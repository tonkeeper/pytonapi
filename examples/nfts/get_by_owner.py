"""Get NFT items by owner address."""
from pytonapi import AsyncTonapi

# Enter your API key
API_KEY = ""  # noqa

# Specify the account ID
ACCOUNT_ID = "EQC-3ilVr-W0Uc3pLrGJElwSaFxvhXXfkiQA3EwdVBHNNess"  # noqa


async def main() -> None:
    tonapi = AsyncTonapi(api_key=API_KEY)
    result = await tonapi.accounts.get_nfts(account_id=ACCOUNT_ID, limit=10)

    for nft in result.nft_items:
        print(f"NFT address (raw): {nft.address.to_raw()}")
        # Output: 0:74c15fd0695c4706213ded4ac45eb7a2f87ff4c8f5d6bc904fe7dd1b735936e4

        print(f"NFT address (user-friendly): {nft.address.to_userfriendly(is_bounceable=True)}")
        # Output: EQB0wV_QaVxHBiE97UrEXrei-H_0yPXWvJBP590bc1k25KtT

        if nft.collection:
            print(f"NFT Collection address: {nft.collection.address.to_userfriendly(is_bounceable=True)}")
            # Output: EQCA14o1-VWhS2efqoh_9M1b_A9DtKTuoqfmkn83AbJzwnPi

        print(f"NFT preview image URL: {nft.previews[0].url}")
        # Output: https://cache.tonapi.io/imgproxy/c0wiqWVwrL...YXJkcy8zMi5wbmc.webp


if __name__ == '__main__':
    import asyncio

    asyncio.run(main())
