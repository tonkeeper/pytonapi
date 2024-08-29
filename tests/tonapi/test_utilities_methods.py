from pytonapi import schema
from tests.tonapi import TestTonapi

ACCOUNT_ID = "EQCD39VS5jcptHL8vMjEXrzGaRcCVYto7HUn4bpAOg8xqB2N"  # noqa


class TestAccountMethod(TestTonapi):

    def test_parse_address(self):
        response = self.tonapi.utilities.parse_address(ACCOUNT_ID)
        self.assertIsInstance(response, schema.utilites.AddressForm)

    def test_status(self):
        response = self.tonapi.utilities.status()
        self.assertIsInstance(response, schema.utilites.ServiceStatus)
