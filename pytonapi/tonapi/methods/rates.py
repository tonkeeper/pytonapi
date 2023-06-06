from typing import List

from pytonapi.schema.rates import Rates
from pytonapi.tonapi import TonapiClient


class RateMethod(TonapiClient):

    def get_prices(self, tokens: List[str], currencies: List[str]) -> Rates:
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
        response = self._get(method=method, params=params)

        return Rates(**response)
