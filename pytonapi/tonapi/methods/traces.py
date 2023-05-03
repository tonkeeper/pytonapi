import base64

from pytonapi.tonapi.client import TonapiClient

from pytonapi.schema.traces import Trace


class TraceMethod(TonapiClient):

    def get_trace(self, trace_id: str) -> Trace:
        """
        Get the trace by trace ID or hash of any transaction in trace.

        :param trace_id: trace ID or transaction hash in hex (without 0x) or base64url format
        :return: :class:`Trace`
        """
        method = f"v2/traces/{base64.b64decode(trace_id).hex()}"
        response = self._request(method=method)

        return Trace(**response)
