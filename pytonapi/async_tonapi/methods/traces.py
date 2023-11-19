import base64
import binascii

from pytonapi.async_tonapi.client import AsyncTonapiClient
from pytonapi.schema.traces import Trace


class TracesMethod(AsyncTonapiClient):

    async def get_trace(self, trace_id: str) -> Trace:
        """
        Get the trace by trace ID or hash of any transaction in trace.

        :param trace_id: trace ID or transaction hash in hex (without 0x) or base64url format
        :return: :class:`Trace`
        """
        if len(trace_id) == 44:
            decoded = base64.urlsafe_b64decode(trace_id + '=' * (-len(trace_id) % 4))
            trace_id = binascii.hexlify(decoded).decode('utf-8')
        method = f"v2/traces/{trace_id}"
        response_data = await self._get(method=method)

        return Trace(**response_data)
