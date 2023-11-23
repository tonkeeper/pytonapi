from typing import List, Callable, Any, Awaitable, Tuple

from pytonapi.async_tonapi.client import AsyncTonapiClient
from pytonapi.schema.events import TransactionEventData, TraceEventData, MempoolEventData


class WebSocketMethod(AsyncTonapiClient):

    async def subscribe_to_transactions(
            self,
            accounts: List[str],
            handler: Callable[[TransactionEventData, ...], Awaitable[Any]],
            args: Tuple[Any, ...] = (),
    ) -> None:
        """
        Subscribes to transactions WebSocket events for the specified accounts.

        :param handler: A callable function to handle the WSMessage
        :param accounts: A list of account addresses to subscribe to
        :param args: Additional arguments to pass to the handler
        """
        method = "subscribe_account"
        params = accounts
        async for data in self._subscribe_websocket(method=method, params=params):
            event = TransactionEventData(**data)
            await handler(event, *args)

    async def subscribe_to_traces(
            self,
            accounts: List[str],
            handler: Callable[[TraceEventData, ...], Awaitable[Any]],
            args: Tuple[Any, ...] = (),
    ) -> None:
        """
        Subscribes to traces WebSocket events for the specified accounts.

        :handler: A callable function to handle the WSMessage
        :accounts: A list of account addresses to subscribe to
        """
        method = "subscribe_trace"
        params = accounts
        async for data in self._subscribe_websocket(method=method, params=params):
            event = TraceEventData(**data)
            await handler(event, *args)

    async def subscribe_to_mempool(
            self,
            accounts: List[str],
            handler: Callable[[MempoolEventData, ...], Awaitable[Any]],
            args: Tuple[Any, ...] = (),
    ) -> None:
        """
        Subscribes to mempool WebSocket events for the specified accounts.

        :handler: A callable function to handle the WSMessage
        :accounts: A list of account addresses to subscribe to
        """
        method = "mempool_message"
        params = accounts
        async for data in self._subscribe_websocket(method=method, params=params):
            event = MempoolEventData(**data)
            await handler(event, *args)
