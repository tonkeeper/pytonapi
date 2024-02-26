from pytonapi import schema
from tests.tonapi import TestTonapi

ACCOUNT_ID = "UQCpfwmPKWkNZ7fpzKrLpJjHzzgo97ABM1kzLN6nHdP2DZQr"  # noqa


class TestInscriptionsMethod(TestTonapi):

    def test_get_all_inscriptions(self):
        response = self.tonapi.inscriptions.get_all_inscriptions(ACCOUNT_ID)
        self.assertIsInstance(response, schema.inscriptions.InscriptionBalances)

    def test_get_inscription_history(self):
        response = self.tonapi.inscriptions.get_inscription_history(ACCOUNT_ID)
        self.assertIsInstance(response, schema.events.AccountEvents)

    def test_get_inscription_history_by_ticker(self):
        response = self.tonapi.inscriptions.get_inscription_history_by_ticker(ACCOUNT_ID, "nano")
        self.assertIsInstance(response, schema.events.AccountEvents)

    def test_create_inscription_comments(self):
        response = self.tonapi.inscriptions.create_inscription_comment(
            ACCOUNT_ID, amount=1000000000, destination=ACCOUNT_ID
        )
        self.assertIsInstance(response, dict)
