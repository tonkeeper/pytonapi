from pytonapi import schema
from tests.tonapi import TestTonapi

ACCOUNT_ID = "EQBCFwW8uFUh-amdRmNY9NyeDEaeDYXd9ggJGsicpqVcHq7B"  # noqa
EVENT_ID = "68656e74d18b10309e41e057191abcfc42f973c82bc84326985cdbf7bf89b126"


class TestJettonMethod(TestTonapi):

    def test_get_info(self):
        response = self.tonapi.jettons.get_info(ACCOUNT_ID)
        self.assertIsInstance(response, schema.jettons.JettonInfo)

    def test_get_holders(self):
        response = self.tonapi.jettons.get_holders(ACCOUNT_ID)
        self.assertIsInstance(response, schema.jettons.JettonHolders)

    def test_get_all_holders(self):
        response = self.tonapi.jettons.get_all_holders(ACCOUNT_ID)
        self.assertIsInstance(response, schema.jettons.JettonHolders)

    def test_get_all_jettons(self):
        response = self.tonapi.jettons.get_all_jettons()
        self.assertIsInstance(response, schema.jettons.Jettons)

    def test_get_jetton_transfer_event(self):
        response = self.tonapi.jettons.get_jetton_transfer_event(EVENT_ID)
        self.assertIsInstance(response, schema.events.Event)
