import base64
import binascii
from typing import Any, Dict, Optional

from pytonapi.base import AsyncTonapiClientBase
from pytonapi.schema.traces import Trace


class TracesMethod(AsyncTonapiClientBase):

    async def get_trace(self, trace_id: str) -> Trace:
        """
        Get the trace by trace ID or hash of any transaction in trace.

        :param trace_id: trace ID or transaction hash in hex (without 0x) or base64url format
        :return: :class:`Trace`
        """
        if len(trace_id) == 44:
            decoded = base64.urlsafe_b64decode(trace_id + "=" * (-len(trace_id) % 4))
            trace_id = binascii.hexlify(decoded).decode("utf-8")
        method = f"v2/traces/{trace_id}"
        response = await self._get(method=method)

        return Trace(**response)

    async def emulate(self, body: Dict[str, Any], ignore_signature_check: Optional[bool] = None) -> Trace:
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
        params = {"ignore_signature_check": ignore_signature_check} if ignore_signature_check else {}
        response = await self._post(method=method, params=params, body=body)

        return Trace(**response)
