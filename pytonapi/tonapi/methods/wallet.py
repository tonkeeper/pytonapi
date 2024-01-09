from typing import Dict, Any, Union

from pytonapi.tonapi.client import TonapiClient
from pytonapi.schema.accounts import Accounts


class WalletMethod(TonapiClient):

    def get_backup_info(
            self,
            x_tonconnect_auth: str,
    ) -> Union[str, None]:
        """
        Get backup info.

        :param x_tonconnect_auth: X-TonConnect-Auth
        :return: :class:`str` dump
        """
        method = "v2/wallet/backup"
        headers = {"X-TonConnect-Auth": x_tonconnect_auth}
        response = self._get(method=method, headers=headers)

        return response.get("dump", None)

    def account_verification(
            self,
            body: Dict[str, Any],
    ) -> Union[str, None]:
        """
        Account verification and token issuance.

        :param body: Data that is expected from TON Connect
            example value:
            {
              "address": "0:97146a46acc2654y27947f14c4a4b14273e954f78bc017790b41208b0043200b",
              "proof": {
                "timestamp": 1678275313,
                "domain": {
                  "length_bytes": 0,
                  "value": "string"
                },
                "signature": "string",
                "payload": "84jHVNLQmZsAAAAAZB0Zryi2wqVJI-KaKNXOvCijEi46YyYzkaSHyJrMPBMOkVZa",
                "state_init": "string"
              }
            }
        :return: :class:`str` token
        """
        method = "v2/wallet/auth/proof"
        response = self._post(method=method, body=body)

        return response.get("token", None)

    def get_by_public_key(
            self,
            public_key: str,
    ) -> Accounts:
        """
        Get wallet by public key.

        :param public_key: Public key
        :return: :class:`Accounts`
        """
        method = f"v2/pubkeys/{public_key}/wallets"
        response = self._get(method=method)

        return Accounts(**response)

    def get_account_seqno(
            self,
            account_id: str,
    ) -> Union[int, None]:
        """
        Get account seqno.

        :param account_id: Account ID
        :return: :class:`int` seqno
        """
        method = f"v2/wallet/{account_id}/seqno"
        response = self._get(method=method)

        return response.get("seqno", None)
