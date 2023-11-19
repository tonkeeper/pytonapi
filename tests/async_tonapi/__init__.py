from unittest import IsolatedAsyncioTestCase

from pytonapi import AsyncTonapi

API_KEY = "YOUR_API_KEY"


class TestAsyncTonapi(IsolatedAsyncioTestCase):

    def setUp(self) -> None:
        self.tonapi = AsyncTonapi(api_key=API_KEY, max_retries=10)
