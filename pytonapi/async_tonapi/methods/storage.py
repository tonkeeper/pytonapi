from pytonapi.async_tonapi.client import AsyncTonapiClient
from pytonapi.schema.storage import StorageProviders


class StorageMethod(AsyncTonapiClient):

    async def get_providers(self) -> StorageProviders:
        """
        Get TON storage providers deployed to the blockchain.

        :return: :class:`StorageProviders`
        """
        method = f"v2/storage/providers"
        response = await self._get(method=method)

        return StorageProviders(**response)
