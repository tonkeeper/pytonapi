from pytonapi import schema
from tests.async_tonapi import TestAsyncTonapi

ACCOUNT_ID = "EQBCFwW8uFUh-amdRmNY9NyeDEaeDYXd9ggJGsicpqVcHq7B"  # noqa


class TestJettonMethod(TestAsyncTonapi):

    async def test_get_info(self):
        response = await self.tonapi.jettons.get_info(ACCOUNT_ID)
        self.assertIsInstance(response, schema.jettons.JettonInfo)
