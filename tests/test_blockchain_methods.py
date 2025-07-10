from pytonapi import schema
from tests import TestAsyncTonapi

PREV_BLOCK_UTIME = 1740393401
NEXT_BLOCK_UTIME = 1740393901
BLOCK_ID = "(-1,8000000000000000,48255809)"
ACCOUNT_ID = "EQBR6UVvw1tFcLkxWapnSQ10QH7JWt1fGUesX_C8lqWbluLL"  # noqa
MESSAGE_ID = "EAC465A0DC51E844B12BBD0040308801FA19B8D1BD49208AA929E2CAAEE9D401"
TRANSACTION_ID = "97264395BD65A255A429B11326C84128B7D70FFED7949ABAE3036D506BA38621"
ACCOUNT_ID_NFT = "EQBSZKEvqoiuPUCFz-CHtpVxAwg1F8PyjZhWAJL2yeujn0_H"  # noqa
MASTERCHATIN_SEQNO = 34835953


class TestBlockchainMethod(TestAsyncTonapi):

    async def test_get_reduced_blocks(self):
        response = await self.tonapi.blockchain.get_reduced_blocks(PREV_BLOCK_UTIME, NEXT_BLOCK_UTIME)
        self.assertIsInstance(response, schema.blockchain.ReducedBlocks)

    async def test_get_block_data(self):
        response = await self.tonapi.blockchain.get_block_data(BLOCK_ID)
        self.assertIsInstance(response, schema.blockchain.BlockchainBlock)

    async def test_get_block_boc(self):
        response = await self.tonapi.blockchain.get_block_boc(BLOCK_ID)
        self.assertIsInstance(response, str)

    async def test_get_block(self):
        response = await self.tonapi.blockchain.get_block(MASTERCHATIN_SEQNO)
        self.assertIsInstance(response, schema.blockchain.BlockchainBlockShards)

    async def test_get_blocks(self):
        response = await self.tonapi.blockchain.get_blocks(MASTERCHATIN_SEQNO)
        self.assertIsInstance(response, schema.blockchain.BlockchainBlocks)

    async def test_get_transactions_shards(self):
        response = await self.tonapi.blockchain.get_transactions_shards(MASTERCHATIN_SEQNO)
        self.assertIsInstance(response, schema.blockchain.Transactions)

    async def test_get_blockchain_config(self):
        response = await self.tonapi.blockchain.get_blockchain_config(MASTERCHATIN_SEQNO)
        self.assertIsInstance(response, schema.blockchain.BlockchainConfig)

    async def test_get_raw_blockchain_config(self):
        response = await self.tonapi.blockchain.get_raw_blockchain_config(MASTERCHATIN_SEQNO)
        self.assertIsInstance(response, schema.blockchain.RawBlockchainConfig)

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
        response = await self.tonapi.blockchain.get_validators()
        self.assertIsInstance(response, schema.blockchain.Validators)

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

    async def test_get_config(self):
        response = await self.tonapi.blockchain.get_config()
        self.assertIsInstance(response, schema.blockchain.BlockchainConfig)

    async def test_get_raw_config(self):
        response = await self.tonapi.blockchain.get_raw_config()
        self.assertIsInstance(response, schema.blockchain.RawBlockchainConfig)

    async def test_execute_get_method(self):
        response = await self.tonapi.blockchain.execute_get_method(
            ACCOUNT_ID_NFT, "get_nft_data")
        self.assertIsInstance(response, schema.blockchain.MethodExecutionResult)
