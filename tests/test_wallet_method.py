from typing import Union

from pytonapi import schema
from tests import TestAsyncTonapi


PUBLIC_KEY = "79c446597dbf81b9987e9059de95dc557bcd9e2c431a6db1677768783d0b99f7"
ACCOUNT_ID = "UQCDrgGaI6gWK-qlyw69xWZosurGxrpRgIgSkVsgahUtxZR0"  # noqa


class TestWalletMethod(TestAsyncTonapi):

    async def test_get_by_public_key(self):
        response = await self.tonapi.wallet.get_by_public_key(PUBLIC_KEY)
        self.assertIsInstance(response, schema.accounts.Accounts)

    async def test_get_account_seqno(self):
        response = await self.tonapi.wallet.get_account_seqno(ACCOUNT_ID)
        self.assertIsInstance(response, Union[int, None])

    async def test_get_info(self):
        response = await self.tonapi.wallet.get_info(ACCOUNT_ID)
        self.assertIsInstance(response, schema.wallet.Wallet)
