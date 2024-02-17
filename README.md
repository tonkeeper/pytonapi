# 📦 PyTONAPI

[![TON](https://img.shields.io/badge/TON-grey?logo=TON&logoColor=40AEF0)](https://ton.org)
[![PyPI](https://img.shields.io/pypi/v/pytonapi.svg?color=FFE873&labelColor=3776AB)](https://pypi.python.org/pypi/pytonapi)
![Python Versions](https://img.shields.io/badge/Python-3.7%20--%203.12-black?color=FFE873&labelColor=3776AB)
[![License](https://img.shields.io/github/license/tonkeeper/pytonapi)](https://github.com/tonkeeper/pytonapi/blob/main/LICENSE)

![Image](https://telegra.ph//file/f88bcf9051073973edbd6.jpg)

![Downloads](https://pepy.tech/badge/pytonapi)
![Downloads](https://pepy.tech/badge/pytonapi/month)
![Downloads](https://pepy.tech/badge/pytonapi/week)

Python SDK for [tonapi.io](https://tonapi.io).\
Information about the API can be found in the  [documentation](https://docs.tonconsole.com/tonapi/api-v2).\
To use the API **you need an API key**, you can get it here [tonconsole.com](https://tonconsole.com/).

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
  Explore a variety of examples in the [examples](https://github.com/tonkeeper/pytonapi/tree/main/examples) folder to
  help you get started and
  understand different use cases.

## Usage

### Installation

```bash
pip install pytonapi
```

### Examples

<details>
<summary><b>Asynchronous</b></summary>

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

</details>

<details>
<summary><b>Synchronous</b></summary>

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

</details>


<details>
<summary><b>More</b></summary>

* Additional examples can be found [examples](https://github.com/tonkeeper/pytonapi/tree/main/examples) folder.

</details>

## Dependencies

* [httpx](https://pypi.org/project/httpx/) - A fully featured HTTP client for Python 3, which provides sync and async
* [pydantic](https://pypi.org/project/pydantic/) - Data validation and settings management using Python type hints
* [websockets](https://pypi.org/project/websockets/) - A library for building WebSocket servers and clients in Python

## Contribution

We welcome your contributions! If you have ideas for improvement or have identified a bug, please create an issue or
submit a pull request.

## Support

Supported by  [TONAPI](https://tonapi.io) and [TON Society](https://github.com/ton-society/grants-and-bounties) (Grants
and Bounties program).

## Donations

**TON** - `EQC-3ilVr-W0Uc3pLrGJElwSaFxvhXXfkiQA3EwdVBHNNess`

**USDT** (TRC-20) - `TJjADKFT2i7jqNJAxkgeRm5o9uarcoLUeR`

## License

This repository is distributed under the [MIT License](https://github.com/tonkeeper/pytonapi/blob/main/LICENSE). Feel
free to use, modify, and distribute the code in accordance
with the terms of the license.

