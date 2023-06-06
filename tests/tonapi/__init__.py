from unittest import TestCase

from pytonapi import Tonapi

API_KEY = "test_key"


class TestTonapi(TestCase):

    def setUp(self) -> None:
        self.tonapi = Tonapi(api_key=API_KEY)  # noqa
