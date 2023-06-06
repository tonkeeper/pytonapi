from pytonapi.tonapi.client import TonapiClient

from pytonapi.schema.jettons import JettonInfo


class JettonMethod(TonapiClient):

    def get_info(self, account_id: str) -> JettonInfo:
        """
        Get jetton metadata by jetton master address.

        :param account_id: account ID
        :return: :class:`JettonInfo`
        """
        method = f"v2/jettons/{account_id}"
        response = self._get(method=method)

        return JettonInfo(**response)
