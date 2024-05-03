"""
You'll need a library for message construction,
such as tonsdk. Below is an example code you can use.
To use the tonsdk library, make sure to install it using pip:

pip install tonsdk
"""

import asyncio

from tonsdk.boc import begin_cell

from pytonapi import AsyncTonapi
from tonsdk.utils import bytes_to_b64str, to_nano
from tonsdk.contract.wallet import Wallets, WalletVersionEnum

# Tonapi Key
API_KEY = "AE33EX7D5...K2AO3FYQ"  # noqa

# Wallet Mnemonics
MNEMONICS = "word1 word2 word3 ..."  # noqa

# Destination Address
DESTINATION_ADDRESS = "EQC...Ness"  # noqa


async def main():
    # Initialize AsyncTonapi with the provided API key and set it to use the testnet or mainnet
    tonapi = AsyncTonapi(api_key=API_KEY, is_testnet=True)

    # Create a wallet from the provided mnemonics
    mnemonics_list = MNEMONICS.split(" ")
    _mnemonics, _pub_k, _priv_k, wallet = Wallets.from_mnemonics(
        mnemonics_list,
        WalletVersionEnum.v4r2,  # Set the version of the wallet
        0,
    )

    # Get the sequence number of the wallet's current state
    method_result = await tonapi.blockchain.execute_get_method(
        wallet.address.to_string(False), "seqno"
    )
    seqno = int(method_result.decoded.get("state", 0))

    # Prepare a transfer message to the destination address with the specified amount and sequence number
    transfer_amount = to_nano(float("0.1"), 'ton')

    # Create the comment payload
    payload = begin_cell().store_uint(0, 32).store_string("Hello World!").end_cell()

    query = wallet.create_transfer_message(
        to_addr=DESTINATION_ADDRESS,
        amount=transfer_amount,
        payload=payload,
        seqno=seqno,
    )

    # Convert the message to Base64 and send it through the Tonapi blockchain
    message_boc = bytes_to_b64str(query["message"].to_boc(False))
    data = {'boc': message_boc}
    await tonapi.blockchain.send_message(data)


if __name__ == "__main__":
    asyncio.run(main())
