from pytonapi.schema.multisig import Multisig
from pytonapi.tonapi.client import TonapiClientBase


class MultisigMethod(TonapiClientBase):

    def get_account_info(self, account_id: str) -> Multisig:
        """
        Get multisig account info.

        :param account_id: account ID
        :return: :class:`AddressForm`
        """
        method = f"v2/multisig/{account_id}"
        response = self._get(method=method)

        return Multisig(**response)
