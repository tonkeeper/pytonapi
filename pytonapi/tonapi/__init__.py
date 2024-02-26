from typing import Any, Dict, Optional

from pytonapi.tonapi.client import TonapiClient
from pytonapi.tonapi import methods

__all__ = [
    "Tonapi",
    "TonapiClient"
]


class Tonapi(TonapiClient):

    def __init__(
            self,
            api_key: str,
            is_testnet: Optional[bool] = False,
            max_retries: Optional[int] = None,
            base_url: Optional[str] = None,
            headers: Optional[Dict[str, Any]] = None,
            timeout: Optional[float] = None,
    ) -> None:
        """
        Initialize the TonapiClient.

        :param api_key: The API key.
        :param base_url: The base URL for the API.
        :param is_testnet: Use True if using the testnet.
        :param timeout: Request timeout in seconds.
        :param headers: Additional headers to include in requests.
        :param max_retries: Maximum number of retries per request if rate limit is reached.
        """
        super().__init__(
            api_key=api_key,
            is_testnet=is_testnet,
            max_retries=max_retries,
            base_url=base_url,
            headers=headers,
            timeout=timeout
        )

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
    def liteserver(self) -> methods.LiteserverMethod:
        return methods.LiteserverMethod(**self.__dict__)

    @property
    def dns(self) -> methods.DnsMethod:
        return methods.DnsMethod(**self.__dict__)

    @property
    def emulate(self) -> methods.EmulateMethod:
        return methods.EmulateMethod(**self.__dict__)

    @property
    def events(self) -> methods.EventsMethod:
        return methods.EventsMethod(**self.__dict__)

    @property
    def inscriptions(self) -> methods.InscriptionsMethod:
        return methods.InscriptionsMethod(**self.__dict__)

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
    def tonconnect(self) -> methods.TonconnectMethod:
        return methods.TonconnectMethod(**self.__dict__)

    @property
    def traces(self) -> methods.TracesMethod:
        return methods.TracesMethod(**self.__dict__)

    @property
    def wallet(self) -> methods.WalletMethod:
        return methods.WalletMethod(**self.__dict__)
