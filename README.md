# PyTONAPI

[![PyPI](https://img.shields.io/pypi/v/pytonapi.svg)](https://pypi.python.org/pypi/pytonapi)
![Python Versions](https://img.shields.io/pypi/pyversions/pytonapi.svg)
![License](https://img.shields.io/github/license/nessshon/pytonapi)

Python wrapper for [tonapi.io](https://tonapi.io/api-v2)\
**Note:** You need an API key to use it, get it here [tonconsole.com](https://tonconsole.com/)

## Features

- **Asynchronous and Synchronous Calls:**\
  Enjoy the flexibility of both asynchronous and synchronous variants for API
  calls.

- **Response Validation with Pydantic Models:**\
  All response data is validated using Pydantic models, ensuring that you
  receive structured and validated information.

- **Convenient Data Manipulation:**\
  The wrapper facilitates seamless manipulation of data, such as converting balances
  to nanotons or amounts.

- **Extensive Examples:**\
  Explore a variety of examples in the [examples](examples) folder to help you get started and
  understand different use cases.

## Dependencies

* [httpx](https://pypi.org/project/httpx/) - A fully featured HTTP client for Python 3, which provides sync and async
* [pydantic](https://pypi.org/project/pydantic/) - Data validation and settings management using Python type hints
* [libscrc](https://pypi.org/project/libscrc/) - Library for calculating CRC-16, CRC-CCITT, CRC-32 checksums
  APIs
* [websockets](https://pypi.org/project/websockets/) - A library for building WebSocket servers and clients in Python

## Installation

```bash
pip install pytonapi
```

## Usage

**Synchronous Example:**

```python
from pytonapi import Tonapi


def main():
    # Create a new Tonapi object with the provided API key
    tonapi = Tonapi(api_key="Your API key")

    # Specify the account ID
    account_id = "EQC-3ilVr-W0Uc3pLrGJElwSaFxvhXXfkiQA3EwdVBHNNess"  # noqa

    # Retrieve account information
    account = tonapi.accounts.get_info(account_id=account_id)

    # Print account details
    print(f"Account Address (raw): {account.address.to_raw()}")
    print(f"Account Address (userfriendly): {account.address.to_userfriendly(is_bounceable=True)}")
    print(f"Account Balance (nanoton): {account.balance.to_nano()}")
    print(f"Account Balance (amount): {account.balance.to_amount()}")


if __name__ == '__main__':
    main()

```

**Asynchronous Example:**

```python
from pytonapi import AsyncTonapi


# Declare an asynchronous function for using await
async def main():
    # Create a new Tonapi object with the provided API key
    tonapi = AsyncTonapi(api_key="Your API key")

    # Specify the account ID
    account_id = "EQC-3ilVr-W0Uc3pLrGJElwSaFxvhXXfkiQA3EwdVBHNNess"  # noqa

    # Retrieve account information asynchronously
    account = await tonapi.accounts.get_info(account_id=account_id)

    # Print account details
    print(f"Account Address (raw): {account.address.to_raw()}")
    print(f"Account Address (userfriendly): {account.address.to_userfriendly(is_bounceable=True)}")
    print(f"Account Balance (nanoton): {account.balance.to_nano()}")
    print(f"Account Balance (amount): {account.balance.to_amount()}")


if __name__ == '__main__':
    import asyncio

    # Run the asynchronous function
    asyncio.run(main())

```

**More Examples:**\
Additional examples can be found in the [examples](examples) folder.

## Donations:

<a href="https://app.tonkeeper.com/transfer/EQC-3ilVr-W0Uc3pLrGJElwSaFxvhXXfkiQA3EwdVBHNNess"><img src="https://telegra.ph//file/8e0ac22311be3fa6f772c.png" width="55"/></a>
<a href="https://tonhub.com/transfer/EQC-3ilVr-W0Uc3pLrGJElwSaFxvhXXfkiQA3EwdVBHNNess"><img src="https://telegra.ph//file/7fa75a1b454a00816d83b.png" width="55"/></a>\
```EQC-3ilVr-W0Uc3pLrGJElwSaFxvhXXfkiQA3EwdVBHNNess```
