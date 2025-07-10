from typing import Any, Dict, Optional

from pytonapi import methods
from pytonapi.base import AsyncTonapiClientBase

__all__ = [
    "AsyncTonapi",
    "AsyncTonapiClientBase",
]


class AsyncTonapi(AsyncTonapiClientBase):

    def __init__(
            self,
            api_key: str,
            is_testnet: bool = False,
            max_retries: int = 0,
            base_url: Optional[str] = None,
            websocket_url: Optional[str] = None,
            headers: Optional[Dict[str, Any]] = None,
            timeout: Optional[float] = None,
            debug: bool = False,
            **kwargs,
    ) -> None:
        """
        Initialize the AsyncTonapiClient.

        :param api_key: The API key.
        :param is_testnet: Use True if using the testnet.
        :param max_retries: Maximum number of retries per request if rate limit is reached.
        :param base_url: The base URL for the API.
        :param websocket_url: The URL for the WebSocket server.
        :param headers: Additional headers to include in requests.
        :param timeout: Request timeout in seconds.
        :param debug: Enable debug mode.
        """
        super().__init__(
            api_key=api_key,
            is_testnet=is_testnet,
            max_retries=max_retries,
            base_url=base_url,
            websocket_url=websocket_url,
            headers=headers,
            timeout=timeout,
            debug=debug,
            **kwargs,
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
    def multisig(self) -> methods.MultisigMethod:
        return methods.MultisigMethod(**self.__dict__)

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
    def gasless(self) -> methods.GaslessMethod:
        return methods.GaslessMethod(**self.__dict__)

    @property
    def nft(self) -> methods.NftMethod:
        return methods.NftMethod(**self.__dict__)

    @property
    def purchases(self) -> methods.PurchasesMethod:
        return methods.PurchasesMethod(**self.__dict__)

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
    def utilities(self) -> methods.UtilitiesMethod:
        return methods.UtilitiesMethod(**self.__dict__)

    @property
    def wallet(self) -> methods.WalletMethod:
        return methods.WalletMethod(**self.__dict__)

    @property
    def webhooks(self) -> methods.WebhooksMethod:
        return methods.WebhooksMethod(**self.__dict__)

    @property
    def websocket(self) -> methods.WebSocketMethod:
        return methods.WebSocketMethod(**self.__dict__)

    @property
    def extra_currency(self) -> methods.ExtraCurrencyMethod:
        return methods.ExtraCurrencyMethod(**self.__dict__)
