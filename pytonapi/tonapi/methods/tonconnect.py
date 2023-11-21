from pytonapi.tonapi.client import TonapiClient
from pytonapi.schema.tonconnect import TonconnectPayload, AccountInfoByStateInit


class TonconnectMethod(TonapiClient):

    def get_payload(self) -> TonconnectPayload:
        """
        Get a payload for further token receipt.

        :return: :class:`TonconnectPayload`
        """
        method = "v2/tonconnect/payload"
        response = self._get(method=method)

        return TonconnectPayload(**response)

    def get_info_by_state_init(self, state_init: str) -> AccountInfoByStateInit:
        """
        Get account info by state init.

        :return: :class:`AccountInfoByStateInit`
        """
        method = "v2/tonconnect/stateinit"
        body = {"state_init": state_init}
        response = self._post(method=method, body=body)

        return AccountInfoByStateInit(**response)
