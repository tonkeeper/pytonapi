from pytonapi import schema
from tests.async_tonapi import TestAsyncTonapi

STATE_INIT = "?"


class TestTonconnectMethod(TestAsyncTonapi):

    async def test_get_payload(self):
        response = await self.tonapi.tonconnect.get_payload()
        self.assertIsInstance(response, schema.tonconnect.TonconnectPayload)

    # async def test_get_info_by_state_init(self):
    #     response = await self.tonapi.tonconnect.get_info_by_state_init(STATE_INIT)
    #     self.assertIsInstance(response, schema.tonconnect.AccountInfoByStateInit)
