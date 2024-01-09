from pprint import pprint

from tests.tonapi import TestTonapi

ACCOUNT_ID = "Ef8zMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzM0vF"
ACCOUNTS_IDS = ["ALL"]


def handler(event) -> None:
    pprint(event)


class TestSSEMethod(TestTonapi):

    def test_subscribe_to_transactions(self):
        self.tonapi.sse.subscribe_to_transactions(ACCOUNTS_IDS, handler)

    def test_subscribe_to_traces(self):
        self.tonapi.sse.subscribe_to_traces(ACCOUNTS_IDS, handler)

    def test_subscribe_to_mempool(self):
        self.tonapi.sse.subscribe_to_mempool([ACCOUNT_ID], handler)
