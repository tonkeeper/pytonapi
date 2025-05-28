from pytonapi.base import AsyncTonapiClientBase
from pytonapi.schema.events import Event
from pytonapi.schema.jettons import JettonInfo, JettonHolders, Jettons, JettonTransferPayload


class JettonsMethod(AsyncTonapiClientBase):

    async def get_info(self, account_id: str) -> JettonInfo:
        """
        Get jetton metadata by jetton master address.

        :param account_id: Account ID
        :return: JettonInfo
        """
        method = f"v2/jettons/{account_id}"
        response = await self._get(method=method)

        return JettonInfo(**response)

    async def get_holders(self, account_id: str, limit: int = 1000, offset: int = 0) -> JettonHolders:
        """
        Get jetton"s holders.

        :param account_id: Account ID
        :param limit: Default value - 1000
        :param offset: Default value - 0
        :return: JettonHolders
        """
        method = f"v2/jettons/{account_id}/holders"
        params = {"limit": limit, "offset": offset}
        response = await self._get(method=method, params=params)

        return JettonHolders(**response)

    async def get_bulk_jettons(self, account_ids: list[str]) -> Jettons:
        """
        Get a list of jetton masters by their addresses.

        :param account_ids: A list of account IDs
        :return: :class:`Jettons`
        """
        method = "v2/jettons/_bulk"
        params = {"account_ids": account_ids}
        response = await self._post(method=method, body=params)

        return Jettons(**response)

    async def get_all_jettons(self, limit: int = 100, offset: int = 0) -> Jettons:
        """
        Get a list of all indexed jetton masters in the blockchain.

        :param limit: Default value - 100
        :param offset: Default value - 0
        :return: :class:`Jettons`
        """
        method = "v2/jettons"
        params = {"limit": limit, "offset": offset}
        response = await self._get(method=method, params=params)

        return Jettons(**response)

    async def get_jetton_transfer_event(self, event_id: str) -> Event:
        """
        Get only jetton transfers in the event.

        :param event_id: event ID or transaction hash in hex (without 0x) or base64url format
        :return: :class:`Event`
        """
        method = f"v2/events/{event_id}/jettons"
        response = await self._get(method=method)

        return Event(**response)

    async def get_jetton_transfer_payload(self, jetton_id: str, account_id: str) -> JettonTransferPayload:
        """
        Get jetton's custom payload and state init required for transfer.

        :param jetton_id: jetton ID
        :param account_id: account ID
        :return: :class:`Event`
        """
        method = f"v2/jettons/{jetton_id}/transfer/{account_id}/payload"
        response = await self._get(method=method)

        return JettonTransferPayload(**response)
