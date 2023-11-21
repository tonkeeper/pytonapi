from pytonapi import schema
from pytonapi.exceptions import TONAPINotImplementedError
from tests.async_tonapi import TestAsyncTonapi

BLOCK_ID = "(-1,8000000000000000,4234234)"
ACCOUNT_ID = "EQBR6UVvw1tFcLkxWapnSQ10QH7JWt1fGUesX_C8lqWbluLL"  # noqa
MESSAGE_ID = "EAC465A0DC51E844B12BBD0040308801FA19B8D1BD49208AA929E2CAAEE9D401"
TRANSACTION_ID = "97264395BD65A255A429B11326C84128B7D70FFED7949ABAE3036D506BA38621"
ACCOUNT_ID_NFT = "EQBSZKEvqoiuPUCFz-CHtpVxAwg1F8PyjZhWAJL2yeujn0_H"  # noqa
MASTERCHATIN_SEQNO = "123456"


class TestBlockchainMethod(TestAsyncTonapi):

    async def test_get_block_data(self):
        response = await self.tonapi.blockchain.get_block_data(BLOCK_ID)
        self.assertIsInstance(response, schema.blockchain.BlockchainBlock)

    async def test_get_block_shards(self):
        response = await self.tonapi.blockchain.get_block_shards(MASTERCHATIN_SEQNO)
        self.assertIsInstance(response, schema.blockchain.BlockchainBlockShards)

    async def test_get_transaction_from_block(self):
        response = await self.tonapi.blockchain.get_transaction_from_block(BLOCK_ID)
        self.assertIsInstance(response, schema.blockchain.Transactions)

    async def test_get_transaction_data(self):
        response = await self.tonapi.blockchain.get_transaction_data(TRANSACTION_ID)
        self.assertIsInstance(response, schema.blockchain.Transaction)

    async def test_get_transaction_by_message(self):
        response = await self.tonapi.blockchain.get_transaction_by_message(MESSAGE_ID)
        self.assertIsInstance(response, schema.blockchain.Transaction)

    async def test_get_validators(self):
        with self.assertRaises(TONAPINotImplementedError) as e:
            await self.tonapi.blockchain.get_validators()
        self.assertEqual(str(e.exception), "not implemented")

    async def test_get_last_masterchain_block(self):
        response = await self.tonapi.blockchain.get_last_masterchain_block()
        self.assertIsInstance(response, schema.blockchain.BlockchainBlock)

    async def test_get_account_info(self):
        response = await self.tonapi.blockchain.get_account_info(ACCOUNT_ID)
        self.assertIsInstance(response, schema.blockchain.BlockchainRawAccount)

    async def test_get_account_transactions(self):
        response = await self.tonapi.blockchain.get_account_transactions(ACCOUNT_ID)
        self.assertIsInstance(response, schema.blockchain.Transactions)

    async def test_inspect_account(self):
        response = await self.tonapi.blockchain.inspect_account(ACCOUNT_ID)
        self.assertIsInstance(response, schema.blockchain.BlockchainAccountInspect)

    async def test_execute_get_method(self):
        response = await self.tonapi.blockchain.execute_get_method(
            ACCOUNT_ID_NFT, "get_nft_data")
        self.assertIsInstance(response, schema.blockchain.MethodExecutionResult)
