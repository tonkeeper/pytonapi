from pytonapi import schema
from pytonapi.exceptions import TONAPIInternalServerError
from tests.async_tonapi import TestAsyncTonapi

DOMAIN_NAME = "foundation.ton"


class TestDNSMethod(TestAsyncTonapi):

    async def test_resolve(self):
        response = await self.tonapi.dns.resolve(domain_name=DOMAIN_NAME)
        self.assertIsInstance(response, schema.dns.DNSRecord)

    async def test_bids(self):
        # response = await self.tonapi.dns.bids(domain_name=VALID_DOMAIN_NAME)
        # self.assertIsInstance(response, schema.domains.DomainBids)

        with self.assertRaises(TONAPIInternalServerError) as e:
            await self.tonapi.dns.bids(DOMAIN_NAME)
        self.assertEqual(str(e.exception), "{'Error': 'not implemented'}")
