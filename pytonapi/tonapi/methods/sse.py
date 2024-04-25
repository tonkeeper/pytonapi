import json
from typing import List, Callable, Any, Tuple

from pytonapi.schema.events import TransactionEventData, TraceEventData, MempoolEventData
from pytonapi.tonapi import TonapiClient


class SSEMethod(TonapiClient):

    def subscribe_to_transactions(
            self,
            accounts: List[str],
            handler: Callable[[TransactionEventData, List[Any]], Any],
            args: Tuple[Any, ...] = (),
    ) -> None:
        """
        Subscribes to transactions SSE events for the specified accounts.

        :param handler: A callable function to handle the SSEEvent
        :param accounts: A list of account addresses to subscribe to
        :param args: Additional arguments to pass to the handler
        """
        method = "v2/sse/accounts/transactions"
        params = {'accounts': accounts}
        for data in self._subscribe(method=method, params=params):
            event = TransactionEventData(**json.loads(data))
            result = handler(event, *args)
            if result is not None:
                return result

    def subscribe_to_traces(
            self,
            accounts: List[str],
            handler: Callable[[TraceEventData, List[Any]], Any],
            args: Tuple[Any, ...] = (),
    ) -> None:
        """
        Subscribes to traces SSE events for the specified accounts.

        :handler: A callable function to handle the SSEEvent
        :accounts: A list of account addresses to subscribe to

        Returns:
            None
        """
        method = "v2/sse/accounts/traces"
        params = {'accounts': accounts}
        for data in self._subscribe(method=method, params=params):
            event = TraceEventData(**json.loads(data))
            result = handler(event, *args)
            if result is not None:
                return result

    def subscribe_to_mempool(
            self,
            accounts: List[str],
            handler: Callable[[MempoolEventData, List[Any]], Any],
            args: Tuple[Any, ...] = (),
    ) -> None:
        """
        Subscribes to mempool SSE events for the specified accounts.

        :handler: A callable function to handle the SSEEvent
        :accounts: A list of account addresses to subscribe to
        """
        method = "v2/sse/mempool"
        params = {'accounts': accounts}
        for data in self._subscribe(method=method, params=params):
            event = MempoolEventData(**json.loads(data))
            result = handler(event, *args)
            if result is not None:
                return result
