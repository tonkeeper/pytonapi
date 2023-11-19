from typing import List, Optional

from pytonapi.async_tonapi.client import AsyncTonapiClient
from pytonapi.schema.rates import ChartRates, Rates


class RatesMethod(AsyncTonapiClient):

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

    async def get_chart(
            self,
            token: str,
            currency: Optional[str] = "USD",
            start_date: Optional[str] = None,
            end_date: Optional[str] = None,
    ) -> ChartRates:
        """
        Get the chart rates for the token to the currency.

        :param token: accept jetton master address
        :param currency: accept fiat currency, example: "USD", "RUB" and so on
        :param start_date: start date (optional)
        :param end_date: end date (optional)
        :return: :class:`ChartRates`
        """
        params = {'token': token, "currency": currency}
        if start_date:
            params["start_date"] = start_date
        if end_date:
            params["end_date"] = end_date
        method = f"v2/rates/chart"
        response = await self._get(method=method, params=params)

        return ChartRates(**response)
