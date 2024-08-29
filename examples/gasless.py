"""
Example of gasless transaction implementation using tonutils with the Tonapi client.

Install tonutils with:
pip install tonutils
"""

from pytoniq_core import Address, Cell
from tonutils.client import TonapiClient
from tonutils.jetton import JettonMaster, JettonWallet
from tonutils.utils import to_nano
from tonutils.wallet import WalletV5R1

from pytonapi import AsyncTonapi

# API key for accessing the Tonapi (obtainable from https://tonconsole.com)
API_KEY = ""

# Mnemonic phrase used to connect the wallet
MNEMONIC: list[str] = []

# USDT master address
USDT_MASTER_ADDRESS = Address("EQCxE6mUtQJKFnGfaROTKOt1lZbDiiX1kCixRv7Nw2Id_sDs")

# Destination address. Replace with a correct recipient address
DESTINATION_ADDRESS = Address("UQC-3ilVr-W0Uc3pLrGJElwSaFxvhXXfkiQA3EwdVBHNNbbp")

# 6 USDT decimals
JETTON_DECIMALS = 6

# Jetton amount for send
JETTON_AMOUNT = to_nano(1, JETTON_DECIMALS)

# Amount for jetton transfer. Usually 0.05 TON is enough for most jetton transfers without forwardBody
BASE_JETTON_SEND_AMOUNT = to_nano(0.05)


async def main() -> None:
    tonapi = AsyncTonapi(API_KEY)
    client = TonapiClient(API_KEY)

    wallet, public_key, private_key, _ = WalletV5R1.from_mnemonic(client, MNEMONIC)
    jetton_wallet_address = await JettonMaster.get_wallet_address(client, wallet.address, USDT_MASTER_ADDRESS)

    gasless_config = await tonapi.gasless.get_config()
    relayer_address = Address(gasless_config.relay_address)

    tether_transfer_body = JettonWallet.build_transfer_body(JETTON_AMOUNT, DESTINATION_ADDRESS, relayer_address)

    message_to_estimate = wallet.create_internal_msg(
        dest=jetton_wallet_address,
        value=BASE_JETTON_SEND_AMOUNT,
        body=tether_transfer_body,
    )

    params = await tonapi.gasless.estimate_gas_price(
        master_id=USDT_MASTER_ADDRESS.to_str(),
        body={
            "wallet_address": wallet.address.to_str(),
            "wallet_public_key": public_key.hex(),
            "messages": [
                {
                    "boc": message_to_estimate.serialize().to_boc().hex(),
                }
            ]
        }
    )

    seqno = await WalletV5R1.get_seqno(client, wallet.address)

    tether_transfer_for_send = wallet.create_signed_internal_msg(
        messages=[
            wallet.create_wallet_internal_message(
                destination=Address(message.address),
                value=int(message.amount),
                body=Cell.one_from_boc(message.payload),
            ) for message in params.messages
        ],
        seqno=seqno,
    )

    ext_message = wallet.create_external_msg(dest=wallet.address, body=tether_transfer_for_send)

    # Send a gasless transfer
    await tonapi.gasless.send(
        body={
            "wallet_public_key": public_key.hex(),
            "boc": ext_message.serialize().to_boc().hex(),
        }
    )


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
