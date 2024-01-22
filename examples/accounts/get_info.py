"""Get account info."""
from pytonapi import Tonapi

# Enter your API key
API_KEY = ""  # noqa

# Specify the account ID
ACCOUNT_ID = "EQAUxYSo-UwoqAGixaD3d7CNLp9PthgmEZfnr6BvsijzJHdA"  # noqa


def main():
    # Creating new Tonapi object
    tonapi = Tonapi(api_key=API_KEY)
    account = tonapi.accounts.get_info(account_id=ACCOUNT_ID)

    print(f"Raw form: {account.address.to_raw()}")
    # output: 0:bede2955afe5b451cde92eb189125c12685c6f8575df922400dc4c1d5411cd35

    print(f"User-friendly: {account.address.to_userfriendly()}")
    # output: UQC-3ilVr-W0Uc3pLrGJElwSaFxvhXXfkiQA3EwdVBHNNbbp

    print(f"User-friendly (bounceable): {account.address.to_userfriendly(is_bounceable=True)}")
    # output: EQC-3ilVr-W0Uc3pLrGJElwSaFxvhXXfkiQA3EwdVBHNNess

    print(f"Balance nanoton: {account.balance.to_nano()}")
    # output: 1500000000

    print(f"Balance TON: {account.balance.to_amount()}")
    # output: 1.5


if __name__ == '__main__':
    main()
