from pytonapi.async_tonapi.client import AsyncTonapiClient
from pytonapi.schema.jettons import JettonInfo


class JettonMethod(AsyncTonapiClient):

    async def get_info(self, account_id: str) -> JettonInfo:
        """
        Get jetton metadata by jetton master address.

        :param account_id: account ID
        :return: :class:`JettonInfo`
        """
        method = f"v2/jettons/{account_id}"
        response = await self._get(method=method)

        return JettonInfo(**response)
