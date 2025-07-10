from pytonapi import schema
from tests import TestAsyncTonapi

ACCOUNT_ID = "UQDNzlh0XSZdb5_Qrlx5QjyZHVAO74v5oMeVVrtF_5Vt1rIt"

class TestPurchasesMethod(TestAsyncTonapi):

    async def test_get_collections(self):
        response = await self.tonapi.purchases.get_purchases_history(ACCOUNT_ID, 1)
        self.assertIsInstance(response, schema.purchases.Purchases)