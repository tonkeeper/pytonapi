from pytonapi import schema
from tests import TestAsyncTonapi

TOKEN = "EQBCFwW8uFUh-amdRmNY9NyeDEaeDYXd9ggJGsicpqVcHq7B"  # noqa
TOKENS = ["TON"]
CURRENCIES = ["USD", "RUB"]


class TestRatesMethod(TestAsyncTonapi):

    async def test_get_rates(self):
        response = await self.tonapi.rates.get_prices(TOKENS, CURRENCIES)
        self.assertIsInstance(response, schema.rates.Rates)

    async def test_get_chart(self):
        response = await self.tonapi.rates.get_chart(TOKEN)
        self.assertIsInstance(response, schema.rates.ChartRates)

    async def test_get_ton_price_from_markets(self):
        response = await self.tonapi.rates.get_ton_price_from_markets()
        self.assertIsInstance(response, schema.rates.MarketsTonRates)
