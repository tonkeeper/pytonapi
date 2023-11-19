from pytonapi.tonapi.client import TonapiClient

from pytonapi.schema.jettons import JettonInfo, JettonHolders, Jettons


class JettonsMethod(TonapiClient):

    def get_info(self, account_id: str) -> JettonInfo:
        """
        Get jetton metadata by jetton master address.

        :param account_id: account ID
        :return: :class:`JettonInfo`
        """
        method = f"v2/jettons/{account_id}"
        response = self._get(method=method)

        return JettonInfo(**response)

    def get_holders(self, account_id: str) -> JettonHolders:
        """
        Get jetton's holders

        :param account_id: account ID
        :return: :class:`JettonHolders`
        """
        method = f"v2/jettons/{account_id}/holders"
        response = self._get(method=method)

        return JettonHolders(**response)

    def get_all_jettons(self, limit: int = 100, offset: int = 0) -> Jettons:
        """
        Get a list of all indexed jetton masters in the blockchain.

        :param limit: Default value - 100
        :param offset: Default value - 0
        :return: :class:`Jettons`
        """
        method = f"v2/jettons"
        params = {"limit": limit, "offset": offset}
        response = self._get(method=method, params=params)

        return Jettons(**response)
