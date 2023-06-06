from pytonapi import schema
from pytonapi.exceptions import TONAPIInternalServerError
from tests.tonapi import TestTonapi

ACCOUNT_ID = "EQCD39VS5jcptHL8vMjEXrzGaRcCVYto7HUn4bpAOg8xqB2N"  # noqa


class TestAccountMethod(TestTonapi):

    def test_get_info(self):
        response = self.tonapi.accounts.get_info(ACCOUNT_ID)
        self.assertIsInstance(response, schema.accounts.Account)

    def test_get_bulk_info(self):
        response = self.tonapi.accounts.get_bulk_info([ACCOUNT_ID])
        self.assertIsInstance(response, schema.accounts.Accounts)

    def test_get_domains(self):
        response = self.tonapi.accounts.get_domains(ACCOUNT_ID)
        self.assertIsInstance(response, schema.domains.DomainNames)

    def test_get_jettons(self):
        response = self.tonapi.accounts.get_jettons_balances(ACCOUNT_ID)
        self.assertIsInstance(response, schema.jettons.JettonsBalances)

    def test_get_nfts(self):
        response = self.tonapi.accounts.get_nfts(ACCOUNT_ID)
        self.assertIsInstance(response, schema.nft.NftItems)

    def test_get_all_nfts(self):
        response = self.tonapi.accounts.get_all_nfts(ACCOUNT_ID)
        self.assertIsInstance(response, schema.nft.NftItems)

    def test_get_traces(self):
        # response = self.tonapi.accounts.get_traces(WALLET_ADDRESS)
        # self.assertIsInstance(response, schema.traces.TraceIds)

        with self.assertRaises(TONAPIInternalServerError) as e:
            self.tonapi.accounts.get_traces(ACCOUNT_ID)
        self.assertEqual(str(e.exception), "{'Error': 'not implemented'}")
