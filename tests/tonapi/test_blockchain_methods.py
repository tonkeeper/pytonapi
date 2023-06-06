from pytonapi import schema
from tests.tonapi import TestTonapi

BLOCK_ID = "(-1,8000000000000000,4234234)"
ACCOUNT_ID = "EQCD39VS5jcptHL8vMjEXrzGaRcCVYto7HUn4bpAOg8xqB2N"  # noqa
TRANSACTION_ID = "97264395BD65A255A429B11326C84128B7D70FFED7949ABAE3036D506BA38621"


class TestBlockchainMethod(TestTonapi):

    def test_get_block_data(self):
        response = self.tonapi.blockchain.get_block_data(BLOCK_ID)
        self.assertIsInstance(response, schema.blockchain.Block)

    def test_get_transaction_from_block(self):
        response = self.tonapi.blockchain.get_transaction_from_block(BLOCK_ID)
        self.assertIsInstance(response, schema.blockchain.Transactions)

    def test_get_transaction_data(self):
        response = self.tonapi.blockchain.get_transaction_data(TRANSACTION_ID)
        self.assertIsInstance(response, schema.blockchain.Transaction)

    def test_get_account_transactions(self):
        response = self.tonapi.blockchain.get_account_transactions(ACCOUNT_ID)
        self.assertIsInstance(response, schema.blockchain.Transactions)
