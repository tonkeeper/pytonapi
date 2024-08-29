from pytonapi import schema
from tests.tonapi import TestTonapi

TOKEN = "EQBCFwW8uFUh-amdRmNY9NyeDEaeDYXd9ggJGsicpqVcHq7B"  # noqa
TOKENS = ["TON"]
CURRENCIES = ["USD", "RUB"]


class TestRatesMethod(TestTonapi):

    def test_get_rates(self):
        response = self.tonapi.rates.get_prices(TOKENS, CURRENCIES)
        self.assertIsInstance(response, schema.rates.Rates)

    def test_get_chart(self):
        response = self.tonapi.rates.get_chart(TOKEN)
        self.assertIsInstance(response, schema.rates.ChartRates)

    def test_get_ton_price_from_markets(self):
        response = self.tonapi.rates.get_ton_price_from_markets()
        self.assertIsInstance(response, schema.rates.MarketsTonRates)
