import asyncio
import json
from typing import Any, Dict, Optional, AsyncGenerator

import httpx
import websockets
from httpx import URL, QueryParams

from pytonapi.exceptions import (
    TONAPIBadRequestError,
    TONAPIError,
    TONAPIInternalServerError,
    TONAPINotFoundError,
    TONAPIUnauthorizedError,
    TONAPITooManyRequestsError,
    TONAPINotImplementedError,
    TONAPISSEError,
)
from pytonapi.logger_config import setup_logging


class AsyncTonapiClientBase:
    """
    Asynchronous TON API Client.
    """

    def __init__(
            self,
            api_key: str,
            is_testnet: bool = False,
            max_retries: int = 0,
            base_url: Optional[str] = None,
            websocket_url: Optional[str] = None,
            headers: Optional[Dict[str, Any]] = None,
            timeout: Optional[float] = None,
            debug: bool = False,
            **kwargs,
    ) -> None:
        """
        Initialize the AsyncTonapiClient.

        :param api_key: The API key.
        :param is_testnet: Use True if using the testnet.
        :param max_retries: Maximum number of retries per request if rate limit is reached.
        :param base_url: The base URL for the API.
        :param websocket_url: The URL for the WebSocket server.
        :param headers: Additional headers to include in requests.
        :param timeout: Request timeout in seconds.
        :param debug: Enable debug mode.
        """
        self.api_key = api_key
        self.is_testnet = is_testnet
        self.timeout = timeout
        self.max_retries = max_retries

        self.base_url = base_url or "https://tonapi.io/" if not is_testnet else "https://testnet.tonapi.io/"
        self.websocket_url = websocket_url or "wss://tonapi.io/v2/websocket"
        self.headers = headers or {"Authorization": f"Bearer {api_key}"}

        self.debug = debug
        self.logger = setup_logging(self.debug)

    @staticmethod
    async def __read_content(response: httpx.Response) -> Any:
        """
        Read the response content.

        :param response: The HTTP response object.
        :return: The response content.
        """
        try:
            data = await response.aread()
            try:
                content = json.loads(data.decode())
            except json.JSONDecodeError:
                content = data.decode()
        except httpx.ResponseNotRead:
            content = {"error": response.text}
        except httpx.ReadError as read_error:
            content = {"error": f"Read error occurred: {read_error}"}
        except Exception as e:
            raise TONAPIError(f"Failed to read response content: {e}")

        return content

    async def __process_response(self, response: httpx.Response) -> Dict[str, Any]:
        """
        Process the HTTP response and handle errors.

        :param response: The HTTP response object.
        :return: The response content as a dictionary.
        :raises TONAPIError: If there is an error status code in the response.
        """
        content = await self.__read_content(response)

        if response.status_code != 200:
            error_map = {
                400: TONAPIBadRequestError,
                401: TONAPIUnauthorizedError,
                403: TONAPIInternalServerError,
                404: TONAPINotFoundError,
                429: TONAPITooManyRequestsError,
                500: TONAPIInternalServerError,
                501: TONAPINotImplementedError,
            }
            error_class = error_map.get(response.status_code, TONAPIError)

            if isinstance(content, dict):
                content = content.get("error") or content.get("Error")
            self.logger.error(f"Error response received: {content}")
            raise error_class(content)

        return content

    async def _subscribe(
            self,
            method: str,
            params: Dict[str, Any],
    ) -> AsyncGenerator[str, None]:
        """
        Subscribe to an SSE event stream.

        :param method: The API method to subscribe to.
        :param params: Optional parameters for the API method.
        """
        url = self.base_url + method
        timeout = httpx.Timeout(timeout=self.timeout)

        self.logger.debug(f"Subscribing to SSE with URL: {url} and params: {params}")
        async with httpx.AsyncClient() as client:
            try:
                async with client.stream(
                        method="GET",
                        url=url,
                        headers=self.headers,
                        params=params or {},
                        timeout=timeout,
                ) as response:
                    response.raise_for_status()

                    async for line in response.aiter_lines():
                        try:
                            key, value = line.split(": ", 1)
                        except ValueError:
                            self.logger.debug(f"Skipped line due to ValueError: {line}")
                            continue
                        if value == "heartbeat":
                            self.logger.debug("Received heartbeat")
                            continue
                        if key == "data":
                            self.logger.debug(f"Received SSE data: {value}")
                            yield value
            except httpx.LocalProtocolError:
                self.logger.error("Local protocol error during SSE subscription.")
                raise TONAPIUnauthorizedError
            except httpx.HTTPStatusError as e:
                self.logger.error(f"HTTP status error during SSE subscription: {e}")
                raise TONAPISSEError(e)

    async def _subscribe_websocket(
            self,
            method: str,
            params: Any,
    ) -> AsyncGenerator[Dict[str, Any], None]:
        """
        Subscribe to a WebSocket event stream.

        :param method: The API method to subscribe to.
        :param params: Parameters for the API method.
        :return: An asynchronous generator yielding WebSocket event data.
        """
        payload = {
            "id": 1,
            "jsonrpc": "2.0",
            "method": method,
            "params": params,
        }
        self.logger.debug("Subscribing to WebSocket with payload: {payload}")
        async with websockets.connect(self.websocket_url) as websocket:
            try:
                await websocket.send(json.dumps(payload))
                while True:
                    message = await websocket.recv()
                    message_json = json.loads(message)
                    if "params" in message_json:
                        value = message_json["params"]
                        self.logger.debug(f"Received WebSocket message: {value}")
                        yield value
            except websockets.exceptions.ConnectionClosed as e:
                self.logger.error(f"WebSocket connection closed unexpectedly: {e}")
                raise TONAPIError(e)

    async def _request(
            self,
            method: str,
            path: str,
            headers: Optional[Dict[str, Any]] = None,
            params: Optional[Dict[str, Any]] = None,
            body: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        Make an HTTP request.

        :param method: The HTTP method (GET or POST).
        :param path: The API path.
        :param headers: Optional headers to include in the request.
        :param params: Optional query parameters.
        :param body: Optional request body data.
        :return: The response content as a dictionary.
        """
        url = self.base_url + path
        self.headers.update(headers or {})
        timeout = httpx.Timeout(timeout=self.timeout)

        self.logger.debug(f"Request {method}: {URL(url).copy_merge_params(QueryParams(params))}")
        self.logger.debug(f"Request headers: {self.headers}")
        if params:
            self.logger.debug(f"Request params: {params}")
        if body:
            self.logger.debug(f"Request body: {body}")
        try:
            async with httpx.AsyncClient(headers=self.headers, timeout=timeout) as session:
                response = await session.request(
                    method=method,
                    url=url,
                    params=params or {},
                    json=body or {},
                )
                response_content = await self.__process_response(response)
                self.logger.debug(f"Response received - Status code: {response.status_code}")
                self.logger.debug(f"Response headers: {response.headers}")
                self.logger.debug(f"Response content: {response_content}")
                return response_content

        except httpx.LocalProtocolError:
            self.logger.error("Local protocol error occurred during request.")
            raise TONAPIUnauthorizedError
        except httpx.HTTPStatusError as e:
            self.logger.error(f"HTTP status error during request: {e}")
            raise TONAPIError(e)

    async def _request_retries(
            self,
            method: str,
            path: str,
            headers: Optional[Dict[str, Any]] = None,
            params: Optional[Dict[str, Any]] = None,
            body: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        Make an HTTP request with retries if rate limit is reached.

        :param method: The HTTP method (GET or POST).
        :param path: The API path.
        :param headers: Optional headers to include in the request.
        :param params: Optional query parameters.
        :param body: Optional request body data.
        :return: The response content as a dictionary.
        """
        for i in range(self.max_retries):
            try:
                return await self._request(
                    method=method,
                    path=path,
                    headers=headers,
                    params=params,
                    body=body,
                )
            except TONAPITooManyRequestsError:
                self.logger.warning(f"Rate limit exceeded. Retrying {i + 1}/{self.max_retries} in 1 second.")
                await asyncio.sleep(1)

        self.logger.error("Max retries exceeded while making request")
        raise TONAPITooManyRequestsError

    async def _get(
            self,
            method: str,
            params: Optional[Dict[str, Any]] = None,
            headers: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        Make a GET request.

        :param method: The API method.
        :param params: Optional query parameters.
        :param headers: Optional headers to include in the request.
        :return: The response content as a dictionary.
        """
        request = self._request
        if self.max_retries > 0:
            request = self._request_retries
        return await request("GET", method, headers, params=params)

    async def _post(
            self,
            method: str,
            params: Optional[Dict[str, Any]] = None,
            body: Optional[Dict[str, Any]] = None,
            headers: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        Make a POST request.

        :param method: The API method.
        :param body: The request body data.
        :param headers: Optional headers to include in the request.
        :return: The response content as a dictionary.
        """
        request = self._request
        if self.max_retries > 0:
            request = self._request_retries
        return await request("POST", method, headers, params=params, body=body)

    async def _delete(
            self,
            method: str,
            params: Optional[Dict[str, Any]] = None,
            headers: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        Make a DELETE request.

        :param method: The API method.
        :param params: Optional query parameters.
        :param headers: Optional headers to include in the request.
        :return: The response content as a dictionary.
        """
        request = self._request
        if self.max_retries > 0:
            request = self._request_retries
        return await request("DELETE", method, headers, params=params)
