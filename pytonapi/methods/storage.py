from pytonapi.base import AsyncTonapiClientBase
from pytonapi.schema.storage import StorageProviders


class StorageMethod(AsyncTonapiClientBase):

    async def get_providers(self) -> StorageProviders:
        """
        Get TON storage providers deployed to the blockchain.

        :return: :class:`StorageProviders`
        """
        method = f"v2/storage/providers"
        response = await self._get(method=method)

        return StorageProviders(**response)
