from pytonapi.async_tonapi import methods
from pytonapi.async_tonapi.client import AsyncTonapiClient

__all__ = [
    "AsyncTonapi",
    "AsyncTonapiClient",
]


class AsyncTonapi(AsyncTonapiClient):

    @property
    def blockchain(self) -> methods.BlockchainMethod:
        return methods.BlockchainMethod(**self.__dict__)

    @property
    def accounts(self) -> methods.AccountsMethod:
        return methods.AccountsMethod(**self.__dict__)

    @property
    def jettons(self) -> methods.JettonsMethod:
        return methods.JettonsMethod(**self.__dict__)

    @property
    def dns(self) -> methods.DnsMethod:
        return methods.DnsMethod(**self.__dict__)

    @property
    def events(self) -> methods.EventsMethod:
        return methods.EventsMethod(**self.__dict__)

    @property
    def nft(self) -> methods.NftMethod:
        return methods.NftMethod(**self.__dict__)

    @property
    def rates(self) -> methods.RatesMethod:
        return methods.RatesMethod(**self.__dict__)

    @property
    def sse(self) -> methods.SSEMethod:
        return methods.SSEMethod(**self.__dict__)

    @property
    def staking(self) -> methods.StakingMethod:
        return methods.StakingMethod(**self.__dict__)

    @property
    def storage(self) -> methods.StorageMethod:
        return methods.StorageMethod(**self.__dict__)

    @property
    def traces(self) -> methods.TracesMethod:
        return methods.TracesMethod(**self.__dict__)
