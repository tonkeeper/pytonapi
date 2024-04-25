from pytonapi import schema
from tests.tonapi import TestTonapi

ACCOUNT_ID = "EQCqFPpSLtcstURtrXLRCv9wyjfrw7_44_nwvD8JiSmSjbUI"


class TestLiteserverMethod(TestTonapi):

    def test_get_account_state(self):
        response = self.tonapi.liteserver.get_account_state(ACCOUNT_ID)
        self.assertIsInstance(response, schema.liteserver.RawAccountState)
