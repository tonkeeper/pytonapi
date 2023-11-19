"""Get account transactions."""
from pytonapi import Tonapi
from pytonapi.utils import nano_to_amount

# Enter your API key
API_KEY = ""  # noqa

# Specify the account ID
ACCOUNT_ID = "EQAUxYSo-UwoqAGixaD3d7CNLp9PthgmEZfnr6BvsijzJHdA"  # noqa


def main():
    # Create a new Tonapi object with the provided API key
    tonapi = Tonapi(api_key=API_KEY)

    # Retrieve account transactions
    result = tonapi.blockchain.get_account_transactions(account_id=ACCOUNT_ID, limit=100)

    # Iterate through transactions and print details
    for transaction in result.transactions:
        # Print transaction value in nanoton
        print(transaction.in_msg.value)
        # Output: 1000000000

        # Print transaction value in amount
        print(nano_to_amount(transaction.in_msg.value))
        # Output: 1.0

        # Print transaction text comment if present
        if transaction.in_msg.decoded_op_name == "text_comment":
            print(transaction.in_msg.decoded_body["text"])
            # Output: Hello, World!


if __name__ == '__main__':
    main()
