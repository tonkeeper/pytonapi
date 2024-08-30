from pytoniq_core import Address, Cell
from tonutils.client import TonapiClient
from tonutils.jetton import JettonMaster, JettonWallet
from tonutils.utils import to_nano
from tonutils.wallet import WalletV5R1

from pytonapi import AsyncTonapi

# API key to access Tonapi (obtained from https://tonconsole.com).
API_KEY = "AE332...2BD5I"

# Mnemonic phrase used to connect the wallet.
MNEMONIC = "a b c ..."

# Jetton master address.
# For this example, USDt.
JETTON_MASTER_ADDRESS = Address("EQCxE6mUtQJKFnGfaROTKOt1lZbDiiX1kCixRv7Nw2Id_sDs")

# Destination address.
# Replace with a correct recipient address.
DESTINATION_ADDRESS = Address("UQC-3ilVr-W0Uc3pLrGJElwSaFxvhXXfkiQA3EwdVBHNNbbp")

# The number of decimal places.
# For USDt, it is 6.
JETTON_DECIMALS = 6

# Jetton amount for send.
# For this example, 1 USDt.
JETTON_AMOUNT = 1

# Amount for jetton transfer.
# Usually 0.05 TON is enough for most jetton transfers without forward_payload.
BASE_JETTON_SEND_AMOUNT = 0.05


async def main() -> None:
    tonapi, client = AsyncTonapi(API_KEY), TonapiClient(API_KEY)

    # We use USDt in this example,
    # so we just print all supported gas jettons and get the relay address.
    # We have to send excess to the relay address in order to make a transfer cheaper.
    relayer_address = await print_config_and_return_relay_address(tonapi)

    wallet, public_key, private_key, _ = WalletV5R1.from_mnemonic(client, MNEMONIC)
    print(f"Wallet address: {wallet.address.to_str()}")

    jetton_wallet_address = await JettonMaster.get_wallet_address(
        client=client,
        owner_address=wallet.address,
        jetton_master_address=JETTON_MASTER_ADDRESS,
    )
    tether_transfer_body = JettonWallet.build_transfer_body(
        jetton_amount=to_nano(JETTON_AMOUNT, JETTON_DECIMALS),
        recipient_address=DESTINATION_ADDRESS,
        response_address=relayer_address,
        # Excess, because some TONs will be sent back to the relay address, commission will be lowered.
    )
    message_to_estimate = wallet.create_internal_msg(
        dest=jetton_wallet_address,
        value=to_nano(BASE_JETTON_SEND_AMOUNT),
        body=tether_transfer_body,
    )

    # We send a single message containing a transfer from our wallet to a desired destination.
    # As a result of estimation, TonAPI returns a list of messages that we need to sign.
    # The first message is a fee transfer to the relay address, the second message is our original transfer.
    sign_raw_params = await tonapi.gasless.estimate_gas_price(
        master_id=JETTON_MASTER_ADDRESS.to_str(),
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

    # Signs Raw Params is the same structure as signRawParams in to connect.
    # OK, at this point, we have everything we need to send a gasless transfer.
    # The message has to be signed internal.
    seqno = await WalletV5R1.get_seqno(client, wallet.address)
    tether_transfer_for_send = wallet.create_signed_internal_msg(
        messages=[
            wallet.create_wallet_internal_message(
                destination=Address(message.address),
                value=int(message.amount),
                body=Cell.one_from_boc(message.payload),
            ) for message in sign_raw_params.messages
        ],
        seqno=seqno,
        valid_until=sign_raw_params.valid_until,
    )
    ext_message = wallet.create_external_msg(
        dest=wallet.address,
        body=tether_transfer_for_send,
    )

    # Send a gasless transfer.
    await tonapi.gasless.send(
        body={
            "wallet_public_key": public_key.hex(),
            "boc": ext_message.serialize().to_boc().hex(),
        }
    )
    print(f"A gasless transfer sent!")


async def print_config_and_return_relay_address(tonapi: AsyncTonapi) -> Address:
    """Fetch the gasless configuration and return the relay address."""
    gasless_config = await tonapi.gasless.get_config()

    print("Available gas jettons:")
    for jetton in gasless_config.gas_jettons:
        print(f"Gas jetton master: {Address(jetton.master_id).to_str()}")

    print(f"Relay address to send fees to: {Address(gasless_config.relay_address).to_str()}")
    return Address(gasless_config.relay_address)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
