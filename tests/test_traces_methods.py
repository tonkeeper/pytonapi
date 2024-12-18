from pytonapi import schema
from tests import TestAsyncTonapi

TRACE_ID_HEX = "97264395BD65A255A429B11326C84128B7D70FFED7949ABAE3036D506BA38621"
TRACE_ID_BASE64 = "VdUG1YMbYqrinFDR4QR7j5CfGQ2O75m34bvxUKvmn00="  # noqa


class TestTraceMethod(TestAsyncTonapi):

    async def test_get_trace(self):
        response = await self.tonapi.traces.get_trace(TRACE_ID_HEX)
        self.assertIsInstance(response, schema.traces.Trace)

        response = await self.tonapi.traces.get_trace(TRACE_ID_BASE64)
        self.assertIsInstance(response, schema.traces.Trace)
