import asyncio
import logging
from typing import Any, Dict

import aiohttp
from aiohttp import ClientResponse

from pytonapi.exceptions import (TONAPIBadRequestError,
                                 TONAPIError, TONAPIInternalServerError,
                                 TONAPINotFoundError, TONAPIUnauthorizedError,
                                 TONAPITooManyRequestsError)


class AsyncTonapiClient:

    def __init__(self, api_key: str, testnet: bool = False, max_retries: int = 3):
        self._api_key = api_key
        self._testnet = testnet
        self._max_retries = max_retries

        self.__headers = {'Authorization': f'Bearer {api_key}'}
        self.__base_url = "https://testnet.tonapi.io/" if testnet else "https://tonapi.io/"

    async def __retry(self, func, *args, **kwargs):
        for i in range(self._max_retries):
            try:
                return await func(*args, **kwargs)
            except TONAPITooManyRequestsError:
                logging.warning(
                    f"Rate limit exceeded. Retrying "
                    f"{i + 1}/{self._max_retries} is in progress."
                )
                await asyncio.sleep(1)

        raise TONAPITooManyRequestsError

    @staticmethod
    async def __process_response(response: ClientResponse) -> Any:
        response_json = await response.json()
        error = response_json.get('error', response_json)

        status_code = response.status
        if status_code == 200:
            return response_json
        elif status_code == 400:
            raise TONAPIBadRequestError(error)
        elif status_code == 401:
            raise TONAPIUnauthorizedError
        elif status_code == 404:
            raise TONAPINotFoundError
        elif status_code == 429:
            raise TONAPITooManyRequestsError(error)
        elif status_code == 500:
            raise TONAPIInternalServerError(error)
        else:
            raise TONAPIError(error)

    async def _get(self, method: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Send a GET request to the TONAPI.

        :param method: The API method to call.
        :param params: The query parameters to include in the request.
        :return: The response data.
        :raises TONAPIBadRequestError: Raised when the client sends a bad request (HTTP 400).
        :raises TONAPIUnauthorizedError: Raised when the client is not authorized to access a resource (HTTP 401).
        :raises TONAPINotFoundError: Raised when the requested resource is not found (HTTP 404).
        :raises TONAPITooManyRequestsError: Raised when the rate limit is exceeded (HTTP 429).
        :raises TONAPIInternalServerError: Raised when the server encounters an internal error (HTTP 500).
        :raises TONAPIError: Raised when the response contains an error.
        """
        params = params.copy() if params is not None else {}

        async with aiohttp.ClientSession(headers=self.__headers) as session:
            url = f"{self.__base_url}{method}"
            async with session.get(url=url, params=params, ssl=False) as response:
                return await self.__retry(self.__process_response, response)

    async def _post(self, method: str, body: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Send a POST request to the TONAPI.

        :param method: The API method to call.
        :param body: The request parameters to include in the request body.
        :return: The response data.
        :raises TONAPIBadRequestError: Raised when the client sends a bad request (HTTP 400).
        :raises TONAPIUnauthorizedError: Raised when the client is not authorized to access a resource (HTTP 401).
        :raises TONAPINotFoundError: Raised when the requested resource is not found (HTTP 404).
        :raises TONAPITooManyRequestsError: Raised when the rate limit is exceeded (HTTP 429).
        :raises TONAPIInternalServerError: Raised when the server encounters an internal error (HTTP 500).
        :raises TONAPIError: Raised when the response contains an error.
        """
        body = body.copy() if body is not None else {}

        async with aiohttp.ClientSession(headers=self.__headers) as session:
            url = f"{self.__base_url}{method}"
            async with session.post(url=url, json=body, ssl=False) as response:
                return await self.__retry(self.__process_response, response)
