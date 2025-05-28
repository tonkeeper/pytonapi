from pytonapi import schema
from tests import TestAsyncTonapi

CURRENCY_ID = 239


class TestExtraCurrencyMethod(TestAsyncTonapi):

    async def test_get_info(self):
        response = await self.tonapi.extra_currency.get_info(CURRENCY_ID)
        self.assertIsInstance(response, schema.extra_currency.EcPreview)
