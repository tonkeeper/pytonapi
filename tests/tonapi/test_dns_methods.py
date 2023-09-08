from pytonapi import schema
from tests.tonapi import TestTonapi

DOMAIN_NAME = "foundation.ton"


class TestDNSMethod(TestTonapi):

    def test_get_info(self):
        response = self.tonapi.dns.get_info(DOMAIN_NAME)
        self.assertIsInstance(response, schema.domains.DomainInfo)

    def test_resolve(self):
        response = self.tonapi.dns.resolve(DOMAIN_NAME)
        self.assertIsInstance(response, schema.dns.DNSRecord)

    def test_bids(self):
        response = self.tonapi.dns.bids(DOMAIN_NAME)
        self.assertIsInstance(response, schema.domains.DomainBids)

    def test_get_auctions(self):
        response = self.tonapi.dns.get_auctions(DOMAIN_NAME)
        self.assertIsInstance(response, schema.dns.Auctions)
