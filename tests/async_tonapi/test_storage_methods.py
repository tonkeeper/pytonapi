from pytonapi import schema
from tests.async_tonapi import TestAsyncTonapi


class TestStorageMethod(TestAsyncTonapi):

    async def test_get_providers(self):
        response = await self.tonapi.storage.get_providers()
        self.assertIsInstance(response, schema.storage.StorageProviders)
