from pytonapi.base import AsyncTonapiClientBase
from pytonapi.schema.utilites import AddressForm, ServiceStatus


class UtilitiesMethod(AsyncTonapiClientBase):

    async def parse_address(self, account_id: str) -> AddressForm:
        """
        parse address and display in all formats.

        :param account_id: account ID
        :return: :class:`AddressForm`
        """
        method = f"v2/address/{account_id}/parse"
        response = await self._get(method=method)

        return AddressForm(**response)

    async def status(self) -> ServiceStatus:
        """
        Reduce indexing latency.

        :return: :class:`ServiceStatus`
        """
        method = "v2/status"
        response = await self._get(method=method)

        return ServiceStatus(**response)
