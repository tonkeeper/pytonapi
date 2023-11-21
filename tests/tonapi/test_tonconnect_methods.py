from pytonapi import schema
from tests.tonapi import TestTonapi

STATE_INIT = "?"


class TestTonconnectMethod(TestTonapi):

    def test_get_payload(self):
        response = self.tonapi.tonconnect.get_payload()
        self.assertIsInstance(response, schema.tonconnect.TonconnectPayload)

    # def test_get_info_by_state_init(self):
    #     response = self.tonapi.tonconnect.get_info_by_state_init(STATE_INIT)
    #     self.assertIsInstance(response, schema.tonconnect.AccountInfoByStateInit)
