from pytonapi import schema
from pytonapi.exceptions import TONAPIInternalServerError, TONAPINotFoundError
from tests.async_tonapi import TestAsyncTonapi

BLOCK_ID = "(-1,8000000000000000,4234234)"
ACCOUNT_ID = "EQCD39VS5jcptHL8vMjEXrzGaRcCVYto7HUn4bpAOg8xqB2N"  # noqa
TRANSACTION_ID = "97264395BD65A255A429B11326C84128B7D70FFED7949ABAE3036D506BA38621"
ACCOUNT_ID_NFT = "EQBSZKEvqoiuPUCFz-CHtpVxAwg1F8PyjZhWAJL2yeujn0_H"  # noqa


class TestBlockchainMethod(TestAsyncTonapi):

    async def test_get_block_data(self):
        response = await self.tonapi.blockchain.get_block_data(BLOCK_ID)
        self.assertIsInstance(response, schema.blockchain.Block)

    async def test_get_transaction_from_block(self):
        response = await self.tonapi.blockchain.get_transaction_from_block(BLOCK_ID)
        self.assertIsInstance(response, schema.blockchain.Transactions)

    async def test_get_transaction_data(self):
        response = await self.tonapi.blockchain.get_transaction_data(TRANSACTION_ID)
        self.assertIsInstance(response, schema.blockchain.Transaction)

    async def test_get_transaction_by_message(self):
        # response = await self.tonapi.blockchain.get_transaction_by_message(TRANSACTION_ID)
        # self.assertIsInstance(response, schema.blockchain.Transaction)

        with self.assertRaises(TONAPINotFoundError) as e:
            await self.tonapi.blockchain.get_transaction_by_message(TRANSACTION_ID)
        self.assertEqual(str(e.exception), "Error 404: Method does not exist.")

    async def test_get_validators(self):
        # response = await self.tonapi.blockchain.get_validators()
        # self.assertIsInstance(response, schema.blockchain.Validators)

        with self.assertRaises(TONAPIInternalServerError) as e:
            await self.tonapi.blockchain.get_validators()
        self.assertEqual(str(e.exception), "{'Error': 'not implemented'}")

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
        # response = await self.tonapi.blockchain.inspect_account(ACCOUNT_ID)
        # self.assertIsInstance(response, schema.blockchain.BlockchainAccountInspect)

        with self.assertRaises(TONAPIInternalServerError) as e:
            await self.tonapi.blockchain.inspect_account(ACCOUNT_ID)
        self.assertEqual(str(e.exception), "not enough refs")

    async def test_execute_get_method(self):
        response = await self.tonapi.blockchain.execute_get_method(
            ACCOUNT_ID_NFT, "get_nft_data")
        self.assertIsInstance(response, schema.blockchain.MethodExecutionResult)
