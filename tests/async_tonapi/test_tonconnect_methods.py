from pytonapi import schema
from tests.async_tonapi import TestAsyncTonapi

STATE_INIT = "?"


class TestTonconnectMethod(TestAsyncTonapi):

    async def test_get_payload(self):
        response = await self.tonapi.tonconnect.get_payload()
        self.assertIsInstance(response, schema.tonconnect.TonconnectPayload)
