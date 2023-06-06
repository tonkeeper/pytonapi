from pytonapi import schema
from tests.tonapi import TestTonapi

TOKENS = ["TON"]
CURRENCIES = ["USD", "RUB"]


class TestRatesMethod(TestTonapi):

    def test_get_rates(self):
        response = self.tonapi.rates.get_prices(TOKENS, CURRENCIES)
        self.assertIsInstance(response, schema.rates.Rates)
