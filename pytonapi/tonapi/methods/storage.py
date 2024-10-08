from pytonapi.tonapi.client import TonapiClientBase
from pytonapi.schema.storage import StorageProviders


class StorageMethod(TonapiClientBase):

    def get_providers(self) -> StorageProviders:
        """
        Get TON storage providers deployed to the blockchain.

        :return: :class:`StorageProviders`
        """
        method = f"v2/storage/providers"
        response = self._get(method=method)

        return StorageProviders(**response)
