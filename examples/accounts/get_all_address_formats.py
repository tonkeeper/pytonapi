"""Parse address and display in all formats."""
from pytonapi import Tonapi

# Enter your API key
API_KEY = ""  # noqa

# Specify the account ID
ACCOUNT_ID = "UQCD39VS5jcptHL8vMjEXrzGaRcCVYto7HUn4bpAOg8xqEBI"  # noqa


def main():
    tonapi = Tonapi(api_key=API_KEY)
    account = tonapi.utilities.parse_address(ACCOUNT_ID)

    print(f"Raw form: {account.raw_form}")
    # output: 0:83dfd552e63729b472fcbcc8c45ebcc6691702558b68ec7527e1ba403a0f31a8

    print(f"Bounceable: {account.bounceable.b64}")
    # output: EQCD39VS5jcptHL8vMjEXrzGaRcCVYto7HUn4bpAOg8xqB2N

    print(f"Non bounceable: {account.non_bounceable.b64}")
    # output: UQCD39VS5jcptHL8vMjEXrzGaRcCVYto7HUn4bpAOg8xqEBI


if __name__ == '__main__':
    main()
