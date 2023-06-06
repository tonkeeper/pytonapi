from pytonapi import schema
from tests.tonapi import TestTonapi

ACCOUNT_ID = "EQBCFwW8uFUh-amdRmNY9NyeDEaeDYXd9ggJGsicpqVcHq7B"  # noqa


class TestJettonMethod(TestTonapi):

    def test_get_info(self):
        response = self.tonapi.jettons.get_info(ACCOUNT_ID)
        self.assertIsInstance(response, schema.jettons.JettonInfo)
