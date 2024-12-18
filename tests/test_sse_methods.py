from pprint import pprint

from tests import TestAsyncTonapi

ACCOUNT_ID = "EQChB2eMoFG4ThuEsZ6ehlBPKJXOjNxlR5B7qKZNGIv256Da"
ACCOUNTS_IDS = ["ALL"]


async def handler(event) -> None:
    pprint(event)


class TestSSEMethod(TestAsyncTonapi):

    async def test_subscribe_to_transactions(self):
        await self.tonapi.sse.subscribe_to_transactions(handler, ACCOUNTS_IDS)

    async def test_subscribe_to_traces(self):
        await self.tonapi.sse.subscribe_to_traces(handler, ACCOUNTS_IDS)

    async def test_subscribe_to_mempool(self):
        await self.tonapi.sse.subscribe_to_mempool(handler, [ACCOUNT_ID])

    async def test_subscribe_to_blocks(self):
        await self.tonapi.sse.subscribe_to_blocks(handler)
