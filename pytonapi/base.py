import asyncio
import json
from typing import Any, Dict, Optional, AsyncGenerator

import aiohttp

from pytonapi.exceptions import (
    TONAPIBadRequestError,
    TONAPIError,
    TONAPIInternalServerError,
    TONAPINotFoundError,
    TONAPIUnauthorizedError,
    TONAPITooManyRequestsError,
    TONAPINotImplementedError,
)
from pytonapi.logger import setup_logging


class AsyncTonapiClientBase:
    """
    Asynchronous TON API Client.
    """

    def __init__(
            self,
            api_key: str,
            is_testnet: bool = False,
            max_retries: int = 0,
            headers: Optional[Dict[str, Any]] = None,
            base_url: Optional[str] = None,
            websocket_url: Optional[str] = None,
            timeout: Optional[float] = None,
            debug: bool = False,
            **kwargs,
    ) -> None:
        """
        Initialize the AsyncTonapiClient.

        :param api_key: The API key.
        :param is_testnet: Use True if using the testnet.
        :param max_retries: Maximum number of retries per request if rate limit is reached.
        :param headers: Additional headers to include in requests.
        :param base_url: The base URL for the API.
        :param websocket_url: The URL for the WebSocket server.
        :param timeout: Request timeout in seconds.
        :param debug: Enable debug mode.
        """
        self.api_key = api_key
        self.is_testnet = is_testnet
        self.max_retries = max(max_retries, 0)

        self.headers = headers or {"Authorization": f"Bearer {self.api_key}"}
        self.base_url = base_url or "https://tonapi.io/" if not is_testnet else "https://testnet.tonapi.io/"
        self.websocket_url = websocket_url or "wss://tonapi.io/v2/websocket"

        self.timeout = timeout
        self.debug = debug
        self.logger = setup_logging(self.debug)

    @staticmethod
    async def __read_content(response: aiohttp.ClientResponse) -> Dict[str, Any]:
        """
        Read the content of a response.

        :param response: The aiohttp response object.
        :return: The response content as a dictionary or a string.
        """
        try:
            content = await response.text()
        except Exception as e:
            raise TONAPIError(f"Failed to read response content: {e}")

        try:
            data = json.loads(content)
            return data.get("error", data)
        except json.JSONDecodeError:
            return {"error": content}

    async def __raise_for_status(self, response: aiohttp.ClientResponse) -> None:
        """
        Raise an exception if the response status code is not 200.

        :param response: The aiohttp response object.
        :raises TONAPIError: If the response status code is not 200.
        """
        if response.status == 200:
            return

        error_map = {
            400: TONAPIBadRequestError,
            401: TONAPIUnauthorizedError,
            403: TONAPIInternalServerError,
            404: TONAPINotFoundError,
            429: TONAPITooManyRequestsError,
            500: TONAPIInternalServerError,
            501: TONAPINotImplementedError,
        }

        error_text = await self.__read_content(response)
        error_class = error_map.get(response.status, TONAPIError)

        self.logger.error(f"Error response received: {error_text}")
        raise error_class(error_text)

    async def _subscribe(
            self,
            method: str,
            params: Dict[str, Any],
    ) -> AsyncGenerator[Dict[str, Any], None]:
        """
        Subscribe to an SSE event stream.

        :param method: The API method to subscribe to.
        :param params: Optional parameters for the API method.
        """
        url = self.base_url + method
        self.logger.debug(f"Subscribing to SSE with URL: {url} and params: {params}")

        try:
            async with aiohttp.ClientSession(headers=self.headers) as session:
                async with session.get(url, params=params or {}, timeout=self.timeout) as response:
                    await self.__raise_for_status(response)

                    async for line in response.content:
                        decoded_line = line.decode("utf-8")
                        line_string = decoded_line.strip()
                        if not line_string:
                            continue

                        try:
                            key, value = line_string.split(": ", 1)
                        except ValueError:
                            self.logger.debug(f"Skipped line due to ValueError: {line_string}")
                            continue

                        if value == "heartbeat":
                            self.logger.debug("Received heartbeat")
                            continue
                        if key == "data":
                            self.logger.debug(f"Received SSE data: {value}")
                            data = json.loads(value)
                            yield data

        except aiohttp.ClientError as e:
            self.logger.error(f"Error subscribing to SSE: {e}")
            raise TONAPIError(e)

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
        self.logger.debug(f"Subscribing to WebSocket with payload: {payload}")

        try:
            async with aiohttp.ClientSession() as session:
                async with session.ws_connect(self.websocket_url) as ws:
                    await ws.send_json(payload)

                    async for msg in ws:
                        if isinstance(msg, aiohttp.WSMessage):
                            if msg.type == aiohttp.WSMsgType.TEXT:
                                message_json = json.loads(msg.data)
                                self.logger.debug(f"Received WebSocket message: {message_json}")
                                if "params" in message_json:
                                    params = message_json["params"]
                                    self.logger.debug(f"Received WebSocket params: {params}")
                                    yield params
                                elif "result" in message_json:
                                    result = message_json["result"]
                                    if not result.startswith("success"):
                                        raise TONAPIError(result)
                            elif msg.type == aiohttp.WSMsgType.CLOSED:
                                self.logger.warning("WebSocket connection closed")
                                break
                            elif msg.type == aiohttp.WSMsgType.ERROR:
                                self.logger.error(f"WebSocket error: {ws.exception()}")
                                raise TONAPIError(f"WebSocket error: {ws.exception()}")
                        else:
                            raise TONAPIError(f"Unexpected WebSocket message type")

        except aiohttp.ClientError as e:
            self.logger.error(f"WebSocket connection failed: {e}")
            raise TONAPIError(e)
        finally:
            if not ws.closed:
                await ws.close()

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

        :param method: The HTTP method (GET, POST, DELETE).
        :param path: The API path.
        :param headers: Optional headers to include in the request.
        :param params: Optional query parameters.
        :param body: Optional request body data.
        :return: The response content as a dictionary.
        """
        url = self.base_url + path
        headers = {**self.headers, **(headers or {})}
        if params:
            params = {k: str(v).lower() if isinstance(v, bool) else v for k, v in params.items()}

        self.logger.debug(f"Request {method}: {url}")
        self.logger.debug(f"Headers: {headers}, Params: {params}, Body: {body}")

        timeout = aiohttp.ClientTimeout(total=self.timeout)

        async with aiohttp.ClientSession(timeout=timeout) as session:
            for attempt in range(self.max_retries + 1):
                try:
                    async with session.request(
                            method=method,
                            url=url,
                            headers=headers,
                            params=params,
                            json=body,
                    ) as response:
                        await self.__raise_for_status(response)
                        return await self.__read_content(response)
                except aiohttp.ClientResponseError as e:
                    self.logger.error(f"Request failed (attempt {attempt}): {e}")
                    if attempt < self.max_retries:
                        await asyncio.sleep(1)
                    else:
                        raise TONAPIError(e)
            else:
                raise TONAPIError("Max retries exceeded")

    async def _get(
            self,
            method: str,
            params: Optional[Dict[str, Any]] = None,
            headers: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Make a GET request."""
        return await self._request("GET", method, params=params, headers=headers)

    async def _post(
            self,
            method: str,
            params: Optional[Dict[str, Any]] = None,
            body: Optional[Dict[str, Any]] = None,
            headers: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Make a POST request."""
        return await self._request("POST", method, params=params, body=body, headers=headers)

    async def _delete(
            self,
            method: str,
            params: Optional[Dict[str, Any]] = None,
            headers: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Make a DELETE request."""
        return await self._request("DELETE", method, params=params, headers=headers)
