from pytonapi import AsyncTonapi
from pytonapi.schema.events import TransactionEventData

# Enter your API key
API_KEY = ""  # noqa

# List of TON blockchain accounts to monitor
ACCOUNTS = [
    "EQBDanbCeUqI4_v-xrnAN0_I2wRvEIaLg1Qg2ZN5c6Zl1KOh",  # noqa
    "UQCtiv7PrMJImWiF2L5oJCgPnzp-VML2CAt5cbn1VsKAxOVB",  # noqa
]


async def handler(event: TransactionEventData, tonapi: AsyncTonapi) -> None:
    """
    Handle SSEvent for transactions.

    :param event: The SSEvent object containing transaction details.
    :param tonapi: An instance of AsyncTonapi for interacting with TON API.
    """
    trace = await tonapi.traces.get_trace(event.tx_hash)

    # If the transaction is successful, print the trace
    if trace.transaction.success:
        print(trace.dict())


async def main() -> None:
    tonapi = AsyncTonapi(api_key=API_KEY)

    # Subscribe to transaction events for the specified accounts
    await tonapi.sse.subscribe_to_transactions(
        accounts=ACCOUNTS, handler=handler, args=(tonapi,)
    )


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
