from pytonapi import schema
from tests import TestAsyncTonapi

ACCOUNT_ID = "UQCDrgGaI6gWK-qlyw69xWZosurGxrpRgIgSkVsgahUtxZR0"  # noqa


class TestWalletMethod(TestAsyncTonapi):

    async def test_get_info(self):
        response = await self.tonapi.wallet.get_info(ACCOUNT_ID)
        self.assertIsInstance(response, schema.wallet.Wallet)
