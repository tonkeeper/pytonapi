import asyncio
import json
import logging
from typing import Any, Dict, Optional, AsyncGenerator

import httpx
import websockets

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


class AsyncTonapiClient:
    """
    Asynchronous TON API Client.
    """

    def __init__(
            self,
            api_key: str,
            is_testnet: Optional[bool] = False,
            max_retries: Optional[int] = None,
            base_url: Optional[str] = None,
            websocket_url: Optional[str] = None,
            headers: Optional[Dict[str, Any]] = None,
            timeout: Optional[float] = None,
    ) -> None:
        """
        Initialize the AsyncTonapiClient.

        :param api_key: The API key.
        :param base_url: The base URL for the API.
        :param websocket_url: The URL for the WebSocket server.
        :param is_testnet: Use True if using the testnet.
        :param timeout: Request timeout in seconds.
        :param headers: Additional headers to include in requests.
        :param max_retries: Maximum number of retries per request if rate limit is reached.
        """
        self.api_key = api_key
        self.is_testnet = is_testnet
        self.timeout = timeout
        self.max_retries = max_retries

        self.base_url = base_url or "https://tonapi.io/" if not is_testnet else "https://testnet.tonapi.io/"
        self.websocket_url = websocket_url or "wss://tonapi.io/v2/websocket"
        self.headers = headers or {"Authorization": f"Bearer {api_key}"}

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
            error_message = content.get("error") if isinstance(content, dict) else content
            raise error_class(error_message)

        return content

    async def _subscribe(
            self,
            method: str,
            params: Optional[Dict[str, Any]],
    ) -> AsyncGenerator[str, None]:
        """
        Subscribe to an SSE event stream.

        :param method: The API method to subscribe to.
        :param params: Optional parameters for the API method.
        """
        url = self.base_url + method
        timeout = httpx.Timeout(timeout=self.timeout)
        data = {"headers": self.headers, "params": params, "timeout": timeout}

        async with httpx.AsyncClient() as client:
            try:
                async with client.stream("GET", url=url, **data) as response:
                    response: httpx.Response
                    response.raise_for_status()

                    async for line in response.aiter_lines():
                        try:
                            key, value = line.split(": ", 1)
                        except ValueError:
                            continue
                        if value == "heartbeat":
                            continue
                        if key == "data":
                            yield value
            except httpx.LocalProtocolError:
                raise TONAPIUnauthorizedError
            except httpx.HTTPStatusError as e:
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
        async with websockets.connect(self.websocket_url) as websocket:
            try:
                await websocket.send(json.dumps(payload))
                while True:
                    message = await websocket.recv()
                    message_json = json.loads(message)
                    if "params" in message_json:
                        value = message_json["params"]
                        yield value
            except websockets.exceptions.ConnectionClosed:
                raise

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
        try:
            async with httpx.AsyncClient(headers=self.headers, timeout=timeout) as session:
                session: httpx.AsyncClient
                data = {"params": params or {}, "json": body or {}}
                response = await session.request(method=method, url=url, **data)
                return await self.__process_response(response)
        except httpx.LocalProtocolError:
            raise TONAPIUnauthorizedError

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
                logging.warning(
                    f"Rate limit exceeded. "
                    f"Retrying {i + 1}/{self.max_retries} is in progress."
                )
                await asyncio.sleep(1)

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
        if self.max_retries:
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
        if self.max_retries:
            request = self._request_retries
        return await request("POST", method, headers, params=params, body=body)
