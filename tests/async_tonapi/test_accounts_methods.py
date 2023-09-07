from pytonapi import schema
from tests.async_tonapi import TestAsyncTonapi

ACCOUNT_ID = "EQCD39VS5jcptHL8vMjEXrzGaRcCVYto7HUn4bpAOg8xqB2N"  # noqa


class TestAccountMethod(TestAsyncTonapi):

    async def test_get_info(self):
        response = await self.tonapi.accounts.get_info(ACCOUNT_ID)
        self.assertIsInstance(response, schema.accounts.Account)

    async def test_get_bulk_info(self):
        response = await self.tonapi.accounts.get_bulk_info([ACCOUNT_ID])
        self.assertIsInstance(response, schema.accounts.Accounts)

    async def test_get_domains(self):
        response = await self.tonapi.accounts.get_domains(ACCOUNT_ID)
        self.assertIsInstance(response, schema.domains.DomainNames)

    async def test_get_jettons(self):
        response = await self.tonapi.accounts.get_jettons_balances(ACCOUNT_ID)
        self.assertIsInstance(response, schema.jettons.JettonsBalances)

    async def test_get_nfts(self):
        response = await self.tonapi.accounts.get_nfts(ACCOUNT_ID)
        self.assertIsInstance(response, schema.nft.NftItems)

    async def test_get_all_nfts(self):
        response = await self.tonapi.accounts.get_all_nfts(ACCOUNT_ID)
        self.assertIsInstance(response, schema.nft.NftItems)

    async def test_get_traces(self):
        response = await self.tonapi.accounts.get_traces(ACCOUNT_ID)
        self.assertIsInstance(response, schema.traces.TraceIds)
