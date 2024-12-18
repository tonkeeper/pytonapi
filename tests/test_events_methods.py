from pytonapi import schema
from tests import TestAsyncTonapi

EVENT_ID_HEX = "53388440417dc044d00e99d89b591acc28f100332a004f180e4f14b876620c13"
EVENT_ID_BASE64 = "5J+GJo3uSr36MjOwjYY+2NzYM7pvnm0WzNQktG8czbM="  # noqa


class TestEventMethod(TestAsyncTonapi):

    async def test_get_event_hex(self):
        response = await self.tonapi.events.get_event(EVENT_ID_HEX)
        self.assertIsInstance(response, schema.events.Event)

    async def test_get_event_base64(self):
        response = await self.tonapi.events.get_event(EVENT_ID_BASE64)
        self.assertIsInstance(response, schema.events.Event)
