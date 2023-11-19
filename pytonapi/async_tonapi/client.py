import asyncio
import json
import logging
from typing import Any, Dict, Optional, Union, AsyncGenerator

import aiohttp
import httpx

from pytonapi.exceptions import (
    TONAPIBadRequestError,
    TONAPIError,
    TONAPIInternalServerError,
    TONAPINotFoundError,
    TONAPIUnauthorizedError,
    TONAPITooManyRequestsError,
    TONAPINotImplementedError
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
            use_ssl: Optional[bool] = None,
            headers: Optional[Dict[str, Any]] = None,
            timeout: Optional[float] = None,
    ) -> None:
        """
        Initialize the AsyncTonapiClient.

        :param api_key: The API key.
        :param base_url: The base URL for the API.
        :param is_testnet: Use True if using the testnet.
        :param use_ssl: Use SSL if True.
        :param timeout: Request timeout in seconds.
        :param headers: Additional headers to include in requests.
        :param max_retries: Maximum number of retries per request if rate limit is reached.
        """
        self.api_key = api_key
        self.use_ssl = use_ssl
        self.timeout = timeout
        self.max_retries = max_retries

        self.base_url = (
            base_url or "https://testnet.tonapi.io/"
            if is_testnet else "https://tonapi.io/"
        )
        self.headers = headers or {"Authorization": f"Bearer {api_key}"}

    @staticmethod
    async def __read_content(
            response: Union[aiohttp.ClientResponse, httpx.Response],
    ) -> Dict[str, Any]:
        """
        Read content from an HTTP response.

        :param response: The HTTP response object.
        :return: The response content as a dictionary.
        :raises TONAPIError: If there is an issue reading the content.
        """

        def try_load_json(c: str) -> Union[Dict, str]:
            """
            Try to load content as JSON. If decoding fails, return the content as a string.

            :param c: The content to be loaded as JSON.
            :return: Decoded JSON content or a dictionary with an 'error' key in case of decoding failure.
            """
            try:
                return json.loads(c)
            except json.JSONDecodeError:
                return {"error": c}

        try:
            content = await response.json()

        except aiohttp.ContentTypeError:
            response: aiohttp.ClientResponse
            content = try_load_json(await response.text())

        except httpx.ResponseNotRead:
            response: httpx.Response
            content_bytes = await response.aread()
            content = try_load_json(content_bytes.decode())

        except Exception as e:
            raise TONAPIError(f"Failed to read response content: {e}")

        return content

    async def __process_response(
            self,
            response: Union[aiohttp.ClientResponse, httpx.Response],
    ) -> Dict[str, Any]:
        """
        Process the HTTP response and handle errors.

        :param response: The HTTP response object.
        :return: The response content as a dictionary.
        :raises TONAPIError: If there is an error status code in the response.
        """
        content = await self.__read_content(response)

        if isinstance(response, aiohttp.ClientResponse):
            status_code = response.status
        else:
            status_code = response.status_code

        if status_code != 200:
            error_map = {
                400: TONAPIBadRequestError,
                401: TONAPIUnauthorizedError,
                404: TONAPINotFoundError,
                429: TONAPITooManyRequestsError,
                500: TONAPIInternalServerError,
                501: TONAPINotImplementedError,
            }
            error_class = error_map.get(status_code, TONAPIError)
            error = content.get("error", content)
            raise error_class(error)

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
                    if response.status_code != 200:
                        await self.__process_response(response)
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
        timeout = aiohttp.ClientTimeout(total=self.timeout)

        async with aiohttp.ClientSession(headers=self.headers, timeout=timeout) as session:
            data = {"params": params or {}, "json": body or {}, "ssl": self.use_ssl}
            async with session.request(method=method, url=url, **data) as response:
                return await self.__process_response(response)

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
        return await request("POST", method, headers, body=body)
