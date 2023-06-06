from pytonapi import schema
from tests.async_tonapi import TestAsyncTonapi

TOKENS = ["TON"]
CURRENCIES = ["USD", "RUB"]


class TestRatesMethod(TestAsyncTonapi):

    async def test_get_rates(self):
        response = await self.tonapi.rates.get_prices(TOKENS, CURRENCIES)
        self.assertIsInstance(response, schema.rates.Rates)
