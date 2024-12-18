from pytonapi import schema
from tests import TestAsyncTonapi

DOMAIN_NAME = "foundation.ton"


class TestDNSMethod(TestAsyncTonapi):

    async def test_get_info(self):
        response = await self.tonapi.dns.get_info(DOMAIN_NAME)
        self.assertIsInstance(response, schema.domains.DomainInfo)

    async def test_resolve(self):
        response = await self.tonapi.dns.resolve(DOMAIN_NAME)
        self.assertIsInstance(response, schema.dns.DNSRecord)

    async def test_bids(self):
        response = await self.tonapi.dns.bids(DOMAIN_NAME)
        self.assertIsInstance(response, schema.domains.DomainBids)

    async def test_get_auctions(self):
        response = await self.tonapi.dns.get_auctions(DOMAIN_NAME)
        self.assertIsInstance(response, schema.dns.Auctions)
