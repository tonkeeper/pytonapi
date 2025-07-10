from pytonapi import schema
from tests import TestAsyncTonapi

MULTISIG_ACCOUNT_ID = "EQD_V-_KzJHIvQGGtgXvY5RcAKZQ16SflviVp2q-ENMO37VD"
ACCOUNT_ORDER_ID = "EQDX-ouflx3eECX-AMeR4jgleD10m1vvrAMgB3ytjV7lrIuW"

class TestMultisigMethod(TestAsyncTonapi):

    async def test_get_account_info(self):
        response = await self.tonapi.multisig.get_account_info(MULTISIG_ACCOUNT_ID)
        self.assertIsInstance(response, schema.multisig.Multisig)

    async def test_get_order_info(self):
        response = await self.tonapi.multisig.get_order_info(ACCOUNT_ORDER_ID)
        self.assertIsInstance(response, schema.multisig.MultisigOrder)
