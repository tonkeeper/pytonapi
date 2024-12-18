from pytonapi import schema
from tests import TestAsyncTonapi

ACCOUNT_ID = "EQCD39VS5jcptHL8vMjEXrzGaRcCVYto7HUn4bpAOg8xqB2N"  # noqa
EVENT_ID = "53388440417dc044d00e99d89b591acc28f100332a004f180e4f14b876620c13"
DOMAIN_NAME = "nessshon.t.me"  # noqa
JETTON_ID = "EQD0vdSA_NedR9uvbgN9EikRX-suesDxGeFg69XQMavfLqIw"  # noqa


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

    async def test_get_jetton(self):
        response = await self.tonapi.accounts.get_jetton_balance(ACCOUNT_ID, JETTON_ID)
        self.assertIsInstance(response, schema.jettons.JettonBalance)

    async def test_get_jettons_history(self):
        response = await self.tonapi.accounts.get_jettons_history(ACCOUNT_ID)
        self.assertIsInstance(response, schema.events.AccountEvents)

    async def test_get_jettons_history_by_jetton(self):
        response = await self.tonapi.accounts.get_jettons_history_by_jetton(ACCOUNT_ID, JETTON_ID)
        self.assertIsInstance(response, schema.events.AccountEvents)

    async def test_get_nfts(self):
        response = await self.tonapi.accounts.get_nfts(ACCOUNT_ID)
        self.assertIsInstance(response, schema.nft.NftItems)

    async def test_get_traces(self):
        response = await self.tonapi.accounts.get_traces(ACCOUNT_ID)
        self.assertIsInstance(response, schema.traces.TraceIds)

    async def test_get_event(self):
        response = await self.tonapi.accounts.get_event(ACCOUNT_ID, EVENT_ID)
        self.assertIsInstance(response, schema.events.AccountEvent)

    async def test_get_events(self):
        response = await self.tonapi.accounts.get_events(ACCOUNT_ID)
        self.assertIsInstance(response, schema.events.AccountEvents)

    async def test_get_nft_history(self):
        response = await self.tonapi.accounts.get_nft_history(ACCOUNT_ID)
        self.assertIsInstance(response, schema.events.AccountEvents)

    async def test_search_by_domain(self):
        response = await self.tonapi.accounts.search_by_domain(DOMAIN_NAME)
        self.assertIsInstance(response, schema.accounts.FoundAccounts)

    async def test_get_subscriptions(self):
        response = await self.tonapi.accounts.get_subscriptions(ACCOUNT_ID)
        self.assertIsInstance(response, schema.accounts.Subscriptions)

    async def test_get_expiring_dns(self):
        response = await self.tonapi.accounts.get_expiring_dns(ACCOUNT_ID)
        self.assertIsInstance(response, schema.accounts.DnsExpiring)

    async def test_get_public_key(self):
        response = await self.tonapi.accounts.get_public_key(ACCOUNT_ID)
        self.assertIsInstance(response, schema.accounts.PublicKey)

    async def test_get_balance_change(self):
        response = await self.tonapi.accounts.get_balance_change(ACCOUNT_ID, 1514746800, 1672513200)
        self.assertIsInstance(response, schema.accounts.BalanceChange)

    async def test_reindex(self):
        response = await self.tonapi.accounts.reindex(ACCOUNT_ID)
        self.assertIs(response, None)
