from typing import Dict, Any, Optional

from pytonapi.schema.blockchain import DecodedMessage
from pytonapi.tonapi.client import TonapiClient
from pytonapi.schema.events import Event, AccountEvent, MessageConsequences
from pytonapi.schema.traces import Trace


class EmulateMethod(TonapiClient):

    def decode_message(self, body: Dict[str, Any]) -> DecodedMessage:
        """
        Decode a given message. Only external incoming messages can be decoded currently.

        :param body: bag-of-cells serialized to base64
            example value:
            {
                "boc": "te6ccgECBQEAARUAAkWIAWTtae+KgtbrX26Bep8JSq8lFLfGOoyGR/xwdjfvpvEaHg"
            }
        :return: :class: `DecodedMessage`
        """
        method = "v2/message/decode"
        response = self._post(
            method=method,
            body=body,
        )
        return DecodedMessage(**response)

    def emulate_events(
            self,
            body: Dict[str, Any],
            accept_language: str = "en",
            ignore_signature_check: Optional[bool] = None,
    ) -> Event:
        """
        Emulate sending message to blockchain.

        :param body: bag-of-cells serialized to base64
            example value:
            {
                 "boc": "te6ccgECBQEAARUAAkWIAWTtae+KgtbrX26Bep8JSq8lFLfGOoyGR/xwdjfvpvEaHg"
            }
        :param accept_language: Default value : en
        :param ignore_signature_check: Default value : None
        :return: :class: `Event`
        """
        method = "v2/events/emulate"
        params = {"ignore_signature_check": ignore_signature_check} if ignore_signature_check else None
        headers = {"Accept-Language": accept_language}
        response = self._post(
            method=method,
            params=params,
            body=body,
            headers=headers,
        )
        return Event(**response)

    def emulate_traces(
            self,
            body: Dict[str, Any],
            ignore_signature_check: Optional[bool] = None,
    ) -> Trace:
        """
        Emulate sending message to blockchain.

        :param body: bag-of-cells serialized to base64
            example value:
            {
                 "boc": "te6ccgECBQEAARUAAkWIAWTtae+KgtbrX26Bep8JSq8lFLfGOoyGR/xwdjfvpvEaHg"
            }
        :param ignore_signature_check: Default value : None
        :return: :class: `Trace`
        """
        method = "v2/traces/emulate"
        params = {"ignore_signature_check": ignore_signature_check} if ignore_signature_check else None
        response = self._post(
            method=method,
            params=params,
            body=body,
        )
        return Trace(**response)

    def emulate_wallet(
            self,
            body: Dict[str, Any],
            accept_language: str = "en",
    ) -> MessageConsequences:
        """
        Emulate sending message to blockchain.

        :param body: bag-of-cells serialized to base64 and additional parameters to configure emulation
            example value:
            {
              "boc": "te6ccgECBQEAARUAAkWIAWTtae+KgtbrX26Bep8JSq8lFLfGOoyGR/xwdjfvpvEaHg",
              "params": [
                {
                  "address": "0:97146a46acc2654y27947f14c4a4b14273e954f78bc017790b41208b0043200b",
                  "balance": 10000000000
                }
              ]
            }
        :param accept_language: Default value : en
        :return: :class: `MessageConsequences`
        """
        method = "v2/wallet/emulate"
        headers = {"Accept-Language": accept_language}
        response = self._post(
            method=method,
            body=body,
            headers=headers,
        )
        return MessageConsequences(**response)

    def emulate_account_event(
            self,
            account_id: str,
            body: Dict[str, Any],
            accept_language: str = "en",
    ) -> AccountEvent:
        """
        Emulate sending message to blockchain.

        :param account_id: account ID
        :param body: bag-of-cells serialized to base64
            example value:
            {
              "boc": "te6ccgECBQEAARUAAkWIAWTtae+KgtbrX26Bep8JSq8lFLfGOoyGR/xwdjfvpvEaHg"
            }
        :param accept_language: Default value : en
        :return: :class: `AccountEvent`
        """
        method = f"v2/accounts/{account_id}/events/emulate"
        headers = {"Accept-Language": accept_language}
        response = self._post(
            method=method,
            body=body,
            headers=headers,
        )
        return AccountEvent(**response)
