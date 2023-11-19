"""Get NFT items by owner address."""
from pytonapi import Tonapi

# Enter your API key
API_KEY = "YOUR_API_KEY"  # noqa

# Specify the account ID
ACCOUNT_ID = "EQC-3ilVr-W0Uc3pLrGJElwSaFxvhXXfkiQA3EwdVBHNNess"  # noqa


def main():
    # Create a new Tonapi object with the provided API key
    tonapi = Tonapi(api_key=API_KEY)

    # Retrieve NFT items for the specified account
    result = tonapi.accounts.get_nfts(account_id=ACCOUNT_ID, limit=10)

    # Iterate through NFT items and print details
    for nft in result.nft_items:
        # Print NFT address in raw format
        print(nft.address.to_raw())
        # Output: 0:74c15fd0695c4706213ded4ac45eb7a2f87ff4c8f5d6bc904fe7dd1b735936e4

        # Print NFT address in user-friendly format
        print(nft.address.to_userfriendly())
        # Output: EQB0wV_QaVxHBiE97UrEXrei-H_0yPXWvJBP590bc1k25KtT

        # Print NFT collection address in user-friendly format
        if nft.collection:
            print(nft.collection.address.to_userfriendly())
        # Output: EQCA14o1-VWhS2efqoh_9M1b_A9DtKTuoqfmkn83AbJzwnPi

        # Print the URL of the first preview image for the NFT
        print(nft.previews[0].url)
        # Output: https://cache.tonapi.io/imgproxy/c0wiqWVwrL...YXJkcy8zMi5wbmc.webp


if __name__ == '__main__':
    main()
