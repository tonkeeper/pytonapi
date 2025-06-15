# 📦 PyTONAPI

[![TON](https://img.shields.io/badge/TON-grey?logo=TON&logoColor=40AEF0)](https://ton.org)
[![PyPI](https://img.shields.io/pypi/v/pytonapi.svg?color=FFE873&labelColor=3776AB)](https://pypi.python.org/pypi/pytonapi)
![Python Versions](https://img.shields.io/badge/Python-3.9%20--%203.13-black?color=FFE873&labelColor=3776AB)
[![License](https://img.shields.io/github/license/tonkeeper/pytonapi)](https://github.com/tonkeeper/pytonapi/blob/main/LICENSE)

![Image](https://telegra.ph//file/f88bcf9051073973edbd6.jpg)

![Downloads](https://pepy.tech/badge/pytonapi)
![Downloads](https://pepy.tech/badge/pytonapi/month)
![Downloads](https://pepy.tech/badge/pytonapi/week)

Python SDK for [tonapi.io](https://tonapi.io).\
Information about the API can be found in the  [documentation](https://docs.tonconsole.com/tonapi/api-v2).\
To use the API **you need an API key**, you can get it here [tonconsole.com](https://tonconsole.com/).

<blockquote>
For creating wallets, transferring TON, Jetton, NFTs, and other operations, recommend using <a href="https://github.com/nessshon/tonutils">tonutils</a> in combination with <code>TonapiClient</code>. For more information, refer to the library documentation.
</blockquote>

## Usage

### Installation

```bash
pip install pytonapi
```

### Examples


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

* **Additional examples** can be found [examples](https://github.com/tonkeeper/pytonapi/tree/main/examples) folder.

## Donations

**TON** - `UQCDrgGaI6gWK-qlyw69xWZosurGxrpRgIgSkVsgahUtxZR0`

**USDT** (TRC-20) - `TDHMG7JRkmJBDD1qd4bNhdfoy2uzVd8ixA`

## Contribution

We welcome your contributions! If you have ideas for improvement or have identified a bug, please create an issue or
submit a pull request.

## Support

Supported by  [TONAPI](https://tonapi.io) and [TON Society](https://github.com/ton-society/grants-and-bounties) (Grants
and Bounties program).

## License

This repository is distributed under the [MIT License](https://github.com/tonkeeper/pytonapi/blob/main/LICENSE). Feel
free to use, modify, and distribute the code in accordance
with the terms of the license.

