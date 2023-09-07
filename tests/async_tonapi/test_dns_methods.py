from pytonapi import schema
from tests.async_tonapi import TestAsyncTonapi

DOMAIN_NAME = "foundation.ton"


class TestDNSMethod(TestAsyncTonapi):

    async def test_resolve(self):
        response = await self.tonapi.dns.resolve(domain_name=DOMAIN_NAME)
        self.assertIsInstance(response, schema.dns.DNSRecord)

    async def test_bids(self):
        response = await self.tonapi.dns.bids(domain_name=DOMAIN_NAME)
        self.assertIsInstance(response, schema.domains.DomainBids)
