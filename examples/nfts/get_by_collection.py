"""Get NFT items from collection by collection address."""
from pytonapi import AsyncTonapi

# Enter your API key
API_KEY = ""  # noqa

# Specify the account ID
ACCOUNT_ID = "EQAUxYSo-UwoqAGixaD3d7CNLp9PthgmEZfnr6BvsijzJHdA"  # noqa


async def main() -> None:
    tonapi = AsyncTonapi(api_key=API_KEY)
    result = await tonapi.nft.get_items_by_collection_address(account_id=ACCOUNT_ID, limit=100)

    for nft in result.nft_items:
        print(f"NFT address (raw): {nft.address.to_raw()}")
        # Output: 0:74c15fd0695c4706213ded4ac45eb7a2f87ff4c8f5d6bc904fe7dd1b735936e4

        print(f"NFT address (user-friendly): {nft.address.to_userfriendly(is_bounceable=True)}")
        # Output: EQC8qwlpFvnbuFaA9BIviVXOwF0E9G9szURiv1RzA0nWz64-

        print(f"NFT owner address: {nft.owner.address.to_userfriendly()}")
        # Output: UQBqRgNG2HCCd6EJCLuduMfYCT3Sne7jFO2fRSZhlcG58YgV

        print(f"NFT preview image URL: {nft.previews[0].url}")
        # Output: https://cache.tonapi.io/imgproxy/c0wiqWVwrL...YXJkcy8zMi5wbmc.webp


if __name__ == '__main__':
    import asyncio

    asyncio.run(main())
