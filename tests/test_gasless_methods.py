from pytonapi import schema
from tests import TestAsyncTonapi

ACCOUNT_ID = "UQCHH6xzGnX6ZlKUt1DW8KCrHfk8ZC8f-ECw88mzwETD5wtk"
PUBLIC_KEY = "71707fe0bafa82f61d4e15ca2b3bb4b82b1c3e2fc844304bcb68e26c96d33c2d"
JETTON_MASTER_ADDRESS = "EQCxE6mUtQJKFnGfaROTKOt1lZbDiiX1kCixRv7Nw2Id_sDs"
MESSAGE_BOC = "b5ee9c7201010201008c000168620056345f955f114491652b9e0fde4e839ca57f5c1e19672fd802e80947e95fc6cd2017d78400000000000000000000000000010100a60f8a7ea5000000000000000030f42408017dbc52ab5fcb68a39bd25d631224b824d0b8df0aebbf244801b8983aa8239a6b0037ef56fa125ff70327f2f7f19da19210377e2b5908f5b5595f66c3a09c35b22b00"

class TestGaslessMethod(TestAsyncTonapi):

    async def test_get_config(self):
        response = await self.tonapi.gasless.get_config()
        self.assertIsInstance(response, schema.gasless.GaslessConfig)

    async def test_estimate_gas_price(self):
        response = await self.tonapi.gasless.estimate_gas_price(
            master_id=JETTON_MASTER_ADDRESS,
            body={
                "wallet_address": ACCOUNT_ID,
                "wallet_public_key": PUBLIC_KEY,
                "messages": [
                    {
                        "boc": MESSAGE_BOC,
                    }
                ]
            }
        )
        self.assertIsInstance(response, schema.gasless.SignRawParams)