from pprint import pprint

from tests.tonapi import TestTonapi

ACCOUNT_ID = "EQChB2eMoFG4ThuEsZ6ehlBPKJXOjNxlR5B7qKZNGIv256Da"
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

    def test_subscribe_to_blocks(self):
        self.tonapi.sse.subscribe_to_blocks(None, handler=handler)
