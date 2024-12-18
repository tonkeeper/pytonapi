from pytonapi import schema
from tests import TestAsyncTonapi

ACCOUNT_ID = "EQCqFPpSLtcstURtrXLRCv9wyjfrw7_44_nwvD8JiSmSjbUI"


class TestLiteserverMethod(TestAsyncTonapi):

    async def test_get_account_state(self):
        response = await self.tonapi.liteserver.get_account_state(ACCOUNT_ID)
        self.assertIsInstance(response, schema.liteserver.RawAccountState)
