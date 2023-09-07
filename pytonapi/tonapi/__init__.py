from pytonapi.tonapi.client import TonapiClient
from pytonapi.tonapi.methods.accounts import AccountMethod
from pytonapi.tonapi.methods.blockchain import BlockchainMethod
from pytonapi.tonapi.methods.dns import DnsMethod
from pytonapi.tonapi.methods.jettons import JettonMethod
from pytonapi.tonapi.methods.nft import NftMethod
from pytonapi.tonapi.methods.rates import RateMethod
from pytonapi.tonapi.methods.traces import TraceMethod


class Tonapi(TonapiClient):

    def __init__(self, api_key: str, testnet: bool = False, max_retries: int = 3):
        """
        :param api_key: You can get an API key here https://tonconsole.com/
        :param testnet: Use true, if you want to switch to testnet
        :param max_retries: Maximum number of retries per request if rate limit is reached
        """
        super().__init__(api_key, testnet, max_retries)

    @property
    def blockchain(self) -> BlockchainMethod:
        return BlockchainMethod(api_key=self._api_key, testnet=self._testnet)

    @property
    def accounts(self) -> AccountMethod:
        return AccountMethod(api_key=self._api_key, testnet=self._testnet)

    @property
    def jettons(self) -> JettonMethod:
        return JettonMethod(api_key=self._api_key, testnet=self._testnet)

    @property
    def dns(self) -> DnsMethod:
        return DnsMethod(api_key=self._api_key, testnet=self._testnet)

    @property
    def nft(self) -> NftMethod:
        return NftMethod(api_key=self._api_key, testnet=self._testnet)

    @property
    def rates(self) -> RateMethod:
        return RateMethod(api_key=self._api_key, testnet=self._testnet)

    @property
    def traces(self) -> TraceMethod:
        return TraceMethod(api_key=self._api_key, testnet=self._testnet)
