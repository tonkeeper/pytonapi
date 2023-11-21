from pytonapi.async_tonapi.client import AsyncTonapiClient
from pytonapi.schema.events import Event
from pytonapi.schema.jettons import JettonInfo, JettonHolders, Jettons


class JettonsMethod(AsyncTonapiClient):

    async def get_info(self, account_id: str) -> JettonInfo:
        """
        Get jetton metadata by jetton master address.

        :param account_id: Account ID
        :return: JettonInfo
        """
        method = f"v2/jettons/{account_id}"
        response = await self._get(method=method)

        return JettonInfo(**response)

    async def get_holders(self, account_id: str) -> JettonHolders:
        """
        Get jetton's holders.

        :param account_id: Account ID
        :return: JettonHolders
        """
        method = f"v2/jettons/{account_id}/holders"
        response = await self._get(method=method)

        return JettonHolders(**response)

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
