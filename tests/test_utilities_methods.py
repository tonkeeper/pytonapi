from pytonapi import schema
from tests import TestAsyncTonapi

ACCOUNT_ID = "EQCD39VS5jcptHL8vMjEXrzGaRcCVYto7HUn4bpAOg8xqB2N"  # noqa


class TestAccountMethod(TestAsyncTonapi):

    async def test_parse_address(self):
        response = await self.tonapi.utilities.parse_address(ACCOUNT_ID)
        self.assertIsInstance(response, schema.utilites.AddressForm)

    async def test_status(self):
        response = await self.tonapi.utilities.status()
        self.assertIsInstance(response, schema.utilites.ServiceStatus)
