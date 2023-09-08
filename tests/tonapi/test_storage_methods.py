from pytonapi import schema
from tests.tonapi import TestTonapi


class TestStorageMethod(TestTonapi):

    def test_get_providers(self):
        response = self.tonapi.storage.get_providers()
        self.assertIsInstance(response, schema.storage.StorageProviders)
