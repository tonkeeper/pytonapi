from pprint import pprint

from tests.async_tonapi import TestAsyncTonapi

ACCOUNT_ID = "Ef8zMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzM0vF"
ACCOUNTS_IDS = ["UQCFJEP4WZ_mpdo0_kMEmsTgvrMHG7K_tWY16pQhKHwoOtFz"]


async def handler(event) -> None:
    pprint(event)


class TestSSEMethod(TestAsyncTonapi):

    async def test_subscribe_to_transactions(self):
        await self.tonapi.websocket.subscribe_to_transactions(handler, ACCOUNTS_IDS)

    async def test_subscribe_to_traces(self):
        await self.tonapi.websocket.subscribe_to_traces(handler, ACCOUNTS_IDS)

    async def test_subscribe_to_mempool(self):
        await self.tonapi.websocket.subscribe_to_mempool(handler, [ACCOUNT_ID])
