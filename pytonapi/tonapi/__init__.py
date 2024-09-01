from typing import Any, Dict, Optional

from pytonapi.tonapi import methods
from pytonapi.tonapi.client import TonapiClientBase

__all__ = [
    "Tonapi",
    "TonapiClientBase"
]


class Tonapi(TonapiClientBase):

    def __init__(
            self,
            api_key: str,
            is_testnet: bool = False,
            max_retries: int = 0,
            base_url: Optional[str] = None,
            headers: Optional[Dict[str, Any]] = None,
            timeout: Optional[float] = None,
            debug: bool = False,
            **kwargs,
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
            timeout=timeout,
            debug=debug,
            **kwargs
        )

    @property
    def __getattributes(self) -> Dict[str, Any]:
        attributes = self.__dict__
        attributes.pop("logger")
        return attributes

    @property
    def blockchain(self) -> methods.BlockchainMethod:
        return methods.BlockchainMethod(**self.__getattributes)

    @property
    def accounts(self) -> methods.AccountsMethod:
        return methods.AccountsMethod(**self.__getattributes)

    @property
    def jettons(self) -> methods.JettonsMethod:
        return methods.JettonsMethod(**self.__getattributes)

    @property
    def liteserver(self) -> methods.LiteserverMethod:
        return methods.LiteserverMethod(**self.__getattributes)

    @property
    def multisig(self) -> methods.MultisigMethod:
        return methods.MultisigMethod(**self.__getattributes)

    @property
    def dns(self) -> methods.DnsMethod:
        return methods.DnsMethod(**self.__getattributes)

    @property
    def emulate(self) -> methods.EmulateMethod:
        return methods.EmulateMethod(**self.__getattributes)

    @property
    def events(self) -> methods.EventsMethod:
        return methods.EventsMethod(**self.__getattributes)

    @property
    def inscriptions(self) -> methods.InscriptionsMethod:
        return methods.InscriptionsMethod(**self.__getattributes)

    @property
    def nft(self) -> methods.NftMethod:
        return methods.NftMethod(**self.__getattributes)

    @property
    def rates(self) -> methods.RatesMethod:
        return methods.RatesMethod(**self.__getattributes)

    @property
    def sse(self) -> methods.SSEMethod:
        return methods.SSEMethod(**self.__getattributes)

    @property
    def staking(self) -> methods.StakingMethod:
        return methods.StakingMethod(**self.__getattributes)

    @property
    def storage(self) -> methods.StorageMethod:
        return methods.StorageMethod(**self.__getattributes)

    @property
    def tonconnect(self) -> methods.TonconnectMethod:
        return methods.TonconnectMethod(**self.__getattributes)

    @property
    def traces(self) -> methods.TracesMethod:
        return methods.TracesMethod(**self.__getattributes)

    @property
    def utilities(self) -> methods.UtilitiesMethod:
        return methods.UtilitiesMethod(**self.__dict__)

    @property
    def wallet(self) -> methods.WalletMethod:
        return methods.WalletMethod(**self.__getattributes)
