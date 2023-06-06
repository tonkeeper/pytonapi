from pytonapi import schema
from tests.tonapi import TestTonapi

TRACE_ID_HEX = "97264395BD65A255A429B11326C84128B7D70FFED7949ABAE3036D506BA38621"  # noqa
TRACE_ID_BASE64 = "Z7wl5ZWqxC5Bs2NWOu-gjNsXOCMAiOiilZDPnV15vCw="  # noqa


class TestTraceMethod(TestTonapi):

    def test_get_trace(self):
        response = self.tonapi.traces.get_trace(TRACE_ID_HEX)
        self.assertIsInstance(response, schema.traces.Trace)

        response = self.tonapi.traces.get_trace(TRACE_ID_BASE64)
        self.assertIsInstance(response, schema.traces.Trace)
