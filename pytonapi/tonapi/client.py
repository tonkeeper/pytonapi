import json
import logging
import time
from typing import Any, Dict, Optional, Generator

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


class TonapiClient:
    """
    Synchronous TON API Client.
    """

    def __init__(
            self,
            api_key: str,
            is_testnet: Optional[bool] = False,
            max_retries: Optional[int] = None,
            base_url: Optional[str] = None,
            headers: Optional[Dict[str, Any]] = None,
            timeout: Optional[float] = None,
    ) -> None:
        """
        Initialize the TonapiClient.

        :param api_key: The API key.
        :param base_url: The base URL for the API.
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
        self.headers = headers or {"Authorization": f"Bearer {api_key}"}

    @staticmethod
    def __read_content(response: httpx.Response) -> Any:
        """
        Read the response content.

        :param response: The HTTP response object.
        :return: The response content.
        """
        try:
            content = response.json()
        except (httpx.ResponseNotRead, json.JSONDecodeError):
            content = {"error": response.text}
        except Exception as e:
            raise TONAPIError(f"Failed to read response content: {e}")

        return content

    def __process_response(self, response: httpx.Response) -> Dict[str, Any]:
        """
        Process the HTTP response and handle errors.

        :param response: The HTTP response object.
        :return: The response content as a dictionary.
        :raises TONAPIError: If there is an error status code in the response.
        """
        content = self.__read_content(response)

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

    def _subscribe(
            self,
            method: str,
            params: Optional[Dict[str, Any]],
    ) -> Generator[str, None, None]:
        """
        Subscribe to an SSE event stream.

        :param method: The API method to subscribe to.
        :param params: Optional parameters for the API method.
        """
        url = self.base_url + method
        timeout = httpx.Timeout(timeout=self.timeout)
        data = {"headers": self.headers, "params": params, "timeout": timeout}

        try:
            with httpx.stream("GET", url=url, **data) as response:
                if response.status_code != 200:
                    self.__process_response(response)
                for line in response.iter_lines():
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

    def _request(
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
            with httpx.Client(headers=self.headers, timeout=timeout) as session:
                session: httpx.Client
                data = {"params": params or {}, "json": body or {}}
                response = session.request(method=method, url=url, **data)
                return self.__process_response(response)
        except httpx.LocalProtocolError:
            raise TONAPIUnauthorizedError

    def _request_retries(
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
                return self._request(
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
                time.sleep(1)
        raise TONAPITooManyRequestsError

    def _get(
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
        return request("GET", method, headers, params=params)

    def _post(
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
        return request("POST", method, headers, params=params, body=body)
