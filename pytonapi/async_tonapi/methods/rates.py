from typing import List

from pytonapi.async_tonapi.client import AsyncTonapiClient
from pytonapi.schema.rates import Rates


class RateMethod(AsyncTonapiClient):

    async def get_prices(self, tokens: List[str], currencies: List[str]) -> Rates:
        """
        Get the token price to the currency.

        :param tokens: Accept TON and jetton master addresses, example:
            ["TON", "EQBCFwW8uFUh-amdRmNY9NyeDEaeDYXd9ggJGsicpqVcHq7B"]
        :param currencies: Accept TON and all possible fiat currencies, example:
            ["TON","USD", "RUB"]
        :return: :class:`Rates`
        """
        params = {
            'tokens': ','.join(map(str, tokens)),
            'currencies': ','.join(map(str, currencies)),
        }
        method = f"v2/rates"
        response = await self._get(method=method, params=params)

        return Rates(**response)
