from pytonapi import schema
from pytonapi.exceptions import TONAPIInternalServerError
from tests.tonapi import TestTonapi

DOMAIN_NAME = "foundation.ton"


class TestDNSMethod(TestTonapi):

    def test_resolve(self):
        response = self.tonapi.dns.resolve(domain_name=DOMAIN_NAME)
        self.assertIsInstance(response, schema.dns.DNSRecord)

    def test_bids(self):
        # response = self.tonapi.dns.bids(domain_name=VALID_DOMAIN_NAME)
        # self.assertIsInstance(response, schema.domains.DomainBids)

        with self.assertRaises(TONAPIInternalServerError) as e:
            self.tonapi.dns.bids(DOMAIN_NAME)
        self.assertEqual(str(e.exception), "{'Error': 'not implemented'}")
