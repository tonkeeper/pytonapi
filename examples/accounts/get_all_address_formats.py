"""Parse address and display in all formats."""
from pytonapi import AsyncTonapi

# Enter your API key
API_KEY = ""  # noqa

# Specify the account ID
ACCOUNT_ID = "UQCD39VS5jcptHL8vMjEXrzGaRcCVYto7HUn4bpAOg8xqEBI"  # noqa


async def main() -> None:
    tonapi = AsyncTonapi(api_key=API_KEY)
    account = await tonapi.utilities.parse_address(ACCOUNT_ID)

    print(f"Raw form: {account.raw_form}")
    # output: 0:83dfd552e63729b472fcbcc8c45ebcc6691702558b68ec7527e1ba403a0f31a8

    print(f"Bounceable: {account.bounceable.b64}")
    # output: EQCD39VS5jcptHL8vMjEXrzGaRcCVYto7HUn4bpAOg8xqB2N

    print(f"Non bounceable: {account.non_bounceable.b64}")
    # output: UQCD39VS5jcptHL8vMjEXrzGaRcCVYto7HUn4bpAOg8xqEBI


if __name__ == '__main__':
    import asyncio

    asyncio.run(main())
