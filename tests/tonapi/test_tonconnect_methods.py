from pytonapi import schema
from tests.tonapi import TestTonapi

STATE_INIT = "?"


class TestTonconnectMethod(TestTonapi):

    def test_get_payload(self):
        response = self.tonapi.tonconnect.get_payload()
        self.assertIsInstance(response, schema.tonconnect.TonconnectPayload)
