from typing import List, Optional

from pytonapi.schema.rates import Rates, ChartRates
from pytonapi.tonapi import TonapiClient


class RatesMethod(TonapiClient):

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

    def get_chart(self, token: str, currency: Optional[str] = "usd",
                  start_date: Optional[str] = None, end_date: Optional[str] = None
                  ) -> ChartRates:
        """
        Get the token price to the currency.

        :param token: accept jetton master address
        :param currency: accept fiat currency, example: "USD", "RUB" and so on
        :param start_date: start date
        :param end_date: end date
        :return: :class:`ChartRates`
        """
        params = {'token': token, "currency": currency}
        if start_date: params["start_date"] = start_date  # noqa:E701
        if end_date: params["end_date"] = end_date  # noqa:E701
        method = f"v2/rates/chart"
        response = self._get(method=method, params=params)

        return ChartRates(**response)
