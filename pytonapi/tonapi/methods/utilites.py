from pytonapi.schema.utilites import AddressForm, ServiceStatus
from pytonapi.tonapi.client import TonapiClientBase


class UtilitiesMethod(TonapiClientBase):

    def parse_address(self, account_id: str) -> AddressForm:
        """
        parse address and display in all formats.

        :param account_id: account ID
        :return: :class:`AddressForm`
        """
        method = f"v2/address/{account_id}/parse"
        response = self._get(method=method)

        return AddressForm(**response)

    def status(self) -> ServiceStatus:
        """
        Reduce indexing latency.

        :return: :class:`ServiceStatus`
        """
        method = "v2/status"
        response = self._get(method=method)

        return ServiceStatus(**response)
