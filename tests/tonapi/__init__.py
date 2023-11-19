from unittest import TestCase

from pytonapi import Tonapi

API_KEY = "YOUR_API_KEY"


class TestTonapi(TestCase):

    def setUp(self) -> None:
        self.tonapi = Tonapi(api_key=API_KEY, max_retries=10)
