import aiohttp

from pytonapi.exceptions import (TONAPIError,
                                 TONAPINotFoundError,
                                 TONAPIBadRequestError,
                                 TONAPIUnauthorizedError,
                                 TONAPIInternalServerError)


class AsyncTonapiClient:

    def __init__(self, api_key: str, testnet: bool = False):
        self._api_key = api_key
        self._testnet = testnet

        self.__headers = {'Authorization': 'Bearer ' + api_key}
        self.__base_url = "https://testnet.tonapi.io/" if testnet else "https://tonapi.io/"

    async def _request(self, method: str, params: dict = None):
        params = params.copy() if params is not None else {}

        async with aiohttp.ClientSession(headers=self.__headers) as session:
            async with await session.get(f"{self.__base_url}{method}",
                                         params=params,
                                         ) as response:
                response_json = await response.json()
                error = response_json.get('error', response_json)

                match response.status:
                    case 200:
                        return response_json
                    case 400:
                        raise TONAPIBadRequestError(error)
                    case 401:
                        raise TONAPIUnauthorizedError
                    case 404:
                        raise TONAPINotFoundError
                    case 500:
                        raise TONAPIInternalServerError(error)

                    case _:
                        raise TONAPIError(error)
