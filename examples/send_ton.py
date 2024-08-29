"""
Simple example of sending TON using tonutils with the Tonapi client.

Install tonutils with:
pip install tonutils
"""

from tonutils.client import TonapiClient
from tonutils.wallet import WalletV4R2

# API key for accessing the Tonapi (obtainable from https://tonconsole.com)
API_KEY = ""

# Set to True for test network, False for main network
IS_TESTNET = True

# Mnemonic phrase used to connect the wallet
MNEMONIC: list[str] = []

# The address of the recipient
DESTINATION_ADDRESS = "UQC-3ilVr-W0Uc3pLrGJElwSaFxvhXXfkiQA3EwdVBHNNbbp"

# Optional comment to include in the forward payload
COMMENT = "Hello from tonutils!"

# Amount to transfer in TON
AMOUNT = 0.01


async def main() -> None:
    client = TonapiClient(api_key=API_KEY, is_testnet=IS_TESTNET)
    wallet, public_key, private_key, mnemonic = WalletV4R2.from_mnemonic(client, MNEMONIC)

    tx_hash = await wallet.transfer(
        destination=DESTINATION_ADDRESS,
        amount=AMOUNT,
        body=COMMENT,
    )

    print(f"Successfully transferred {AMOUNT} TON!")
    print(f"Transaction hash: {tx_hash}")


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
