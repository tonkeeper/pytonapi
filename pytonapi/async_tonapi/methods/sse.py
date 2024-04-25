import json
from typing import List, Callable, Any, Awaitable, Tuple, Optional

from pytonapi.async_tonapi.client import AsyncTonapiClient
from pytonapi.schema.events import TransactionEventData, TraceEventData, MempoolEventData


class SSEMethod(AsyncTonapiClient):

    async def subscribe_to_transactions(
            self,
            handler: Callable[[TransactionEventData, List[Any]], Awaitable[Any]],
            accounts: List[str],
            operations: Optional[List[str]] = None,
            args: Tuple[Any, ...] = (),
    ) -> Any:
        """
        Subscribes to transactions SSE events for the specified accounts.

        :param handler: A callable function to handle the SSEEvent
        :param accounts: A comma-separated list of account IDs.
         A special value of "accounts" is ALL. TonAPI will stream transactions for all accounts in this case.
        :param operations: A comma-separated list of operations, which makes it possible
         to get transactions based on the `first 4 bytes of a message body of an inbound message(opens in a new tab)
         <https://docs.ton.org/develop/smart-contracts/guidelines/internal-messages#internal-message-body>`_.
         Each operation is a string containing either one of the supported names or a hex string
         representing a message operation opcode which is an unsigned 32-bit integer.
         A hex string must start with "0x" prefix and have exactly 8 hex digits.
         An example of "operations" is &operations=JettonTransfer,0x0524c7ae,StonfiSwap.
         The advantage of using hex strings is that it's possible to get transactions for operations
         that are not yet present on `the list <https://github.com/tonkeeper/tongo/blob/master/abi/messages.md>`_.
        :param args: Additional arguments to pass to the handler
        """
        method = "v2/sse/accounts/transactions"
        params = {'accounts': ",".join(accounts)}
        if operations:
            params['operations'] = ",".join(operations)

        async for data in self._subscribe(method=method, params=params):
            event = TransactionEventData(**json.loads(data))
            result = await handler(event, *args)
            if result is not None:
                return result

    async def subscribe_to_traces(
            self,
            accounts: List[str],
            handler: Callable[[TraceEventData, List[Any]], Awaitable[Any]],
            args: Tuple[Any, ...] = (),
    ) -> Any:
        """
        Subscribes to traces SSE events for the specified accounts.

        :handler: A callable function to handle the SSEEvent
        :accounts: A list of account addresses to subscribe to
        """
        method = "v2/sse/accounts/traces"
        params = {'accounts': ",".join(accounts)}
        async for data in self._subscribe(method=method, params=params):
            event = TraceEventData(**json.loads(data))
            result = await handler(event, *args)
            if result is not None:
                return result

    async def subscribe_to_mempool(
            self,
            accounts: List[str],
            handler: Callable[[MempoolEventData, List[Any]], Awaitable[Any]],
            args: Tuple[Any, ...] = (),
    ) -> Any:
        """
        Subscribes to mempool SSE events for the specified accounts.

        :handler: A callable function to handle the SSEEvent
        :accounts: A list of account addresses to subscribe to
        """
        method = "v2/sse/mempool"
        params = {'accounts': ",".join(accounts)}
        async for data in self._subscribe(method=method, params=params):
            event = MempoolEventData(**json.loads(data))
            result = await handler(event, *args)
            if result is not None:
                return result
