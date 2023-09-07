from pytonapi import schema
from tests.tonapi import TestTonapi

DOMAIN_NAME = "foundation.ton"


class TestDNSMethod(TestTonapi):

    def test_resolve(self):
        response = self.tonapi.dns.resolve(domain_name=DOMAIN_NAME)
        self.assertIsInstance(response, schema.dns.DNSRecord)

    def test_bids(self):
        response = self.tonapi.dns.bids(domain_name=DOMAIN_NAME)
        self.assertIsInstance(response, schema.domains.DomainBids)
