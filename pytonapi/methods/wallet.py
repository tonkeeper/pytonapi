from typing import Dict, Any, Union

from pytonapi.base import AsyncTonapiClientBase
from pytonapi.schema.accounts import Accounts
from pytonapi.schema.events import MessageConsequences
from pytonapi.schema.wallet import Wallet


class WalletMethod(AsyncTonapiClientBase):

    async def account_verification(
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
        response = await self._post(method=method, body=body)

        return response.get("token", None)

    async def get_by_public_key(
            self,
            public_key: str,
    ) -> Accounts:
        """
        Get wallet by public key.

        :param public_key: Public key
        :return: :class:`Accounts`
        """
        method = f"v2/pubkeys/{public_key}/wallets"
        response = await self._get(method=method)

        return Accounts(**response)

    async def get_account_seqno(
            self,
            account_id: str,
    ) -> Union[int, None]:
        """
        Get account seqno.

        :param account_id: Account ID
        :return: :class:`int` seqno
        """
        method = f"v2/wallet/{account_id}/seqno"
        response = await self._get(method=method)

        return response.get("seqno", None)

    async def emulate(self, body: Dict[str, Any], accept_language: str = "en") -> MessageConsequences:
        """
        Emulate sending message to blockchain.

        :param body: Data that is expected. example value:
                    {
                      "boc": "string",
                      "params": [
                        {
                          "address": "0:97146a46acc2654y27947f14c4a4b14273e954f78bc017790b41208b0043200b",
                          "balance": 10000000000
                        }
                      ]
                    }
        :param accept_language: Default value: en
        :return: :class:`Dict[str, Any]`
        """
        method = "v2/wallet/emulate"
        headers = {"Accept-Language": accept_language}
        response = await self._post(method=method, body=body, headers=headers)

        return MessageConsequences(**response)

    async def get_info(self, account_id: str) -> Wallet:
        """
        Get human-friendly information about a wallet without low-level details.

        :param account_id: Account ID
        :return: :class:`Wallet`
        """
        method = f"v2/wallet/{account_id}"
        response = await self._get(method=method)

        return Wallet(**response)
