"""Get NFT items from collection by collection address."""
from pytonapi import Tonapi

# Enter your API key
API_KEY = "YOUR_API_KEY"  # noqa

# Specify the account ID
ACCOUNT_ID = "EQAUxYSo-UwoqAGixaD3d7CNLp9PthgmEZfnr6BvsijzJHdA"  # noqa


def main():
    # Create a new Tonapi object with the provided API key
    tonapi = Tonapi(api_key=API_KEY)

    # Retrieve NFT items by collection address
    result = tonapi.nft.get_items_by_collection_address(account_id=ACCOUNT_ID, limit=100)

    # Iterate through NFT items and print details
    for nft in result.nft_items:
        # Print NFT address in raw format
        print(nft.address.to_raw())
        # Output: 0:74c15fd0695c4706213ded4ac45eb7a2f87ff4c8f5d6bc904fe7dd1b735936e4

        # Print NFT address in user-friendly format
        print(nft.address.to_userfriendly())
        # Output: EQB0wV_QaVxHBiE97UrEXrei-H_0yPXWvJBP590bc1k25KtT

        # Print NFT owner's user-friendly address
        print(nft.owner.address.to_userfriendly(is_bounceable=True))
        # Output: UQBqRgNG2HCCd6EJCLuduMfYCT3Sne7jFO2fRSZhlcG58YgV

        # Print the URL of the first preview image for the NFT
        print(nft.previews[0].url)
        # Output: https://cache.tonapi.io/imgproxy/c0wiqWVwr79OCcmR7qD-4WIKWOnk8t4vX_cqmohhE8s/rs:fill:100:100:1/g:no/aHR0cHM6Ly9uZnQudG9ubWVuZG9uLmNvbS9jb2xsZWN0aW9ucy9jYXJkcy8zMi5wbmc.webp


if __name__ == '__main__':
    main()
