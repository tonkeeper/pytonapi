from unittest import IsolatedAsyncioTestCase

from pytonapi import AsyncTonapi

API_KEY = ""  # noqa


class TestAsyncTonapi(IsolatedAsyncioTestCase):

    def setUp(self) -> None:
        self.tonapi = AsyncTonapi(api_key=API_KEY, debug=True)
