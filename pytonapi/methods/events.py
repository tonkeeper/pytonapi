import base64
import binascii
from typing import Any, Dict, Optional

from pytonapi.base import AsyncTonapiClientBase
from pytonapi.schema.events import Event


class EventsMethod(AsyncTonapiClientBase):

    async def get_event(self, event_id: str, accept_language: str = "en") -> Event:
        """
        Get an event either by event ID or a hash of any transaction in a trace.
        An event is built on top of a trace which is a series of transactions caused
        by one inbound message. TonAPI looks for known patterns inside the trace and
        splits the trace into actions, where a single action represents a meaningful
        high-level operation like a Jetton Transfer or an NFT Purchase.
        Actions are expected to be shown to users. It is advised not to build any logic
        on top of actions because actions can be changed at any time.

        :param event_id: event ID
        :param accept_language: Default value : en
        :return: :class:`Event`
        """
        if len(event_id) == 44:
            decoded = base64.urlsafe_b64decode(event_id + "=" * (-len(event_id) % 4))
            event_id = binascii.hexlify(decoded).decode("utf-8")
        method = f"v2/events/{event_id}"
        headers = {"Accept-Language": accept_language}
        response = await self._get(method=method, headers=headers)

        return Event(**response)

    async def emulate(
            self, body: Dict[str, Any],
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
        params = {"ignore_signature_check": ignore_signature_check} if ignore_signature_check else {}
        headers = {"Accept-Language": accept_language}
        response = await self._post(method=method, params=params, body=body, headers=headers)

        return Event(**response)
