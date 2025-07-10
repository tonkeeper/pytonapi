from typing import Union

from pytonapi import schema
from tests import TestAsyncTonapi


BLOCK_ID = "(-1,8000000000000000,49704923,4580369e736daf8d81811f50ed361e71c44b66329b6ac398bec72a37eae70a38,f93d671179786fb06f828bede74fd9c7ee7c495a9b36a69d0ed9d0ccdfe7c045)"
ACCOUNT_ID = "UQCHH6xzGnX6ZlKUt1DW8KCrHfk8ZC8f-ECw88mzwETD5wtk"
ELECTOR_ID = "Ef8zMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzM0vF"
ELECTOR_TX_LT = 59246012000001
TX_LT = 59226897000003
TX_HASH = "d21670e5482219d407692ffc5def6354baefcbc9ceef326d786954b63c90cd6a"

class TestGaslessMethod(TestAsyncTonapi):

    async def test_get_masterchain_info(self):
        response = await self.tonapi.liteserver.get_masterchain_info()
        self.assertIsInstance(response, schema.liteserver.RawMasterChainInfo)

    async def test_get_masterchain_info_ext(self):
        response = await self.tonapi.liteserver.get_masterchain_info_ext(0)
        self.assertIsInstance(response, schema.liteserver.RawMasterChainInfoExt)

    async def test_get_time(self):
        response = await self.tonapi.liteserver.get_time()
        self.assertIsInstance(response, Union[int, None])

    async def test_get_raw_block(self):
        response = await self.tonapi.liteserver.get_raw_block(BLOCK_ID)
        self.assertIsInstance(response, schema.liteserver.RawGetBlock)

    async def test_get_raw_header(self):
        response = await self.tonapi.liteserver.get_raw_header(BLOCK_ID, 0)
        self.assertIsInstance(response, schema.liteserver.RawBlockHeader)

    async def test_get_account_state(self):
        response = await self.tonapi.liteserver.get_account_state(ACCOUNT_ID)
        self.assertIsInstance(response, schema.liteserver.RawAccountState)

    async def test_get_shard_info(self):
        response = await self.tonapi.liteserver.get_shard_info(BLOCK_ID, -1, 8000000000000000, False)
        self.assertIsInstance(response, schema.liteserver.RawShardInfo)

    async def test_get_all_raw_shards_info(self):
        response = await self.tonapi.liteserver.get_all_raw_shards_info(BLOCK_ID)
        self.assertIsInstance(response, schema.liteserver.RawShardsInfo)

    async def test_get_raw_transactions(self):
        response = await self.tonapi.liteserver.get_raw_transactions(ACCOUNT_ID, TX_LT, TX_HASH, 1)
        self.assertIsInstance(response, schema.liteserver.RawTransactions)

    async def test_get_raw_list_block_transaction(self):
        response = await self.tonapi.liteserver.get_raw_list_block_transaction(BLOCK_ID, 0, 1)
        self.assertIsInstance(response, schema.liteserver.RawListBlockTransactions)

    async def test_get_block_proof(self):
        response = await self.tonapi.liteserver.get_block_proof(BLOCK_ID, 0)
        self.assertIsInstance(response, schema.liteserver.RawBlockProof)

    async def test_get_config_all(self):
        response = await self.tonapi.liteserver.get_config_all(BLOCK_ID, 0)
        self.assertIsInstance(response, schema.liteserver.RawConfig)

    async def test_get_shard_block_proof(self):
        response = await self.tonapi.liteserver.get_shard_block_proof(BLOCK_ID)
        self.assertIsInstance(response, schema.liteserver.RawShardProof)

    async def test_get_out_msg_queue_size(self):
        response = await self.tonapi.liteserver.get_out_msg_queue_size()
        self.assertIsInstance(response, schema.liteserver.OutMsgQueueSize)
