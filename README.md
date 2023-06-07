# PyTONAPI
[![PyPI](https://img.shields.io/pypi/v/pytonapi.svg)](https://pypi.python.org/pypi/pytonapi)
![Python Versions](https://img.shields.io/pypi/pyversions/pytonapi.svg)
![License](https://img.shields.io/github/license/nessshon/pytonapi)

Python wrapper for [tonapi.io](https://tonapi.io/swagger-ui/v2) v2
\
__You need an api key to use it, get it here [tonconsole.com](https://tonconsole.com/)__

### Dependencies

* [aiohttp](https://pypi.org/project/aiohttp/)
* [requests](https://pypi.org/project/requests/)
* [pydantic](https://pypi.org/project/pydantic/)
* [libscrc](https://pypi.org/project/libscrc/)


### Installation

```bash
pip install pytonapi
```

### Examples

Get account info:

```python
# Importing required package
from pytonapi import Tonapi


def main():
    # Creating new Tonapi object
    tonapi = Tonapi(api_key="Your api key")

    account_id = "EQC-3ilVr-W0Uc3pLrGJElwSaFxvhXXfkiQA3EwdVBHNNess"  # noqa
    account = tonapi.accounts.get_info(account_id=account_id)

    # print account address (raw)
    print(account.address.to_raw())
    # output: 0:bede2955afe5b451cde92eb189125c12685c6f8575df922400dc4c1d5411cd35

    # print account address (userfriendly)
    print(account.address.to_userfriendly())
    # output: EQC-3ilVr-W0Uc3pLrGJElwSaFxvhXXfkiQA3EwdVBHNNess

    # print account balance (nanoton)
    print(account.balance.to_nano())
    # output: 1500000000

    # print account balance (amount)
    print(account.balance.to_amount())
    # output: 1.5


if __name__ == '__main__':
    main()
```

#### Asynchronous example:

```python
# Importing required package
import asyncio

from pytonapi import AsyncTonapi


# Declaring asynchronous function for using await
async def main():
    # Creating new Tonapi object
    tonapi = AsyncTonapi(api_key="Your api key")

    account_id = "EQC-3ilVr-W0Uc3pLrGJElwSaFxvhXXfkiQA3EwdVBHNNess"  # noqa
    account = await tonapi.accounts.get_info(account_id=account_id)

    # print account address (raw)
    print(account.address.to_raw())
    # output: 0:bede2955afe5b451cde92eb189125c12685c6f8575df922400dc4c1d5411cd35

    # print account address (userfriendly)
    print(account.address.to_userfriendly())
    # output: EQC-3ilVr-W0Uc3pLrGJElwSaFxvhXXfkiQA3EwdVBHNNess

    # print account balance (nanoton)
    print(account.balance.to_nano())
    # output: 1500000000

    # print account balance (amount)
    print(account.balance.to_amount())
    # output: 1.5


if __name__ == '__main__':
    # Running asynchronous function
    asyncio.run(main())

```

\
Get account transactions:

```python
# Importing required package
from pytonapi import Tonapi
from pytonapi.utils import nano_to_amount


def main():
    # Creating new Tonapi object
    tonapi = Tonapi(api_key="Your api key")

    account_id = "EQC-3ilVr-W0Uc3pLrGJElwSaFxvhXXfkiQA3EwdVBHNNess"  # noqa
    result = tonapi.blockchain.get_account_transactions(
        account_id=account_id, limit=100,
    )
    for transaction in result.transactions:

        # print transaction value (nanoton)
        print(transaction.in_msg.value)
        # output: 1000000000

        # print transaction value (amount)
        print(nano_to_amount(transaction.in_msg.value))
        # output: 1.0

        # print transaction text comment
        if transaction.in_msg.decoded_op_name == "text_comment":
            print(transaction.in_msg.decoded_body["Text"])
            # output: Hello, World!


if __name__ == '__main__':
    main()
```

\
Get NFT items from collection by collection address:

```python
# Importing required package
from pytonapi import Tonapi


def main():
    # Creating new Tonapi object
    tonapi = Tonapi(api_key="Your api key")

    account_id = "EQAUxYSo-UwoqAGixaD3d7CNLp9PthgmEZfnr6BvsijzJHdA"  # noqa
    result = tonapi.nft.get_items_by_collection_address(
        account_id=account_id, limit=100, offset=0
    )
    for nft in result.nft_items:
        # print nft address (raw)
        print(nft.address.to_raw())
        # output: 0:74c15fd0695c4706213ded4ac45eb7a2f87ff4c8f5d6bc904fe7dd1b735936e4

        # print nft address (userfriendly)
        print(nft.address.to_userfriendly())
        # output: EQB0wV_QaVxHBiE97UrEXrei-H_0yPXWvJBP590bc1k25KtT

        # print nft owner address
        print(nft.owner.address.to_userfriendly())
        # output: EQCOF6xKqliQjY1yrwwn7qm8OjyEJBpH_sqVCe-XgMak5MDN

        # print nft previews url
        print(nft.previews[0].url)
        # output: https://cache.tonapi.io/imgproxy/c0wiqWVwr79OCcmR7qD-4WIKWOnk8t4vX_cqmohhE8s/rs:fill:100:100:1/g:no/aHR0cHM6Ly9uZnQudG9ubWVuZG9uLmNvbS9jb2xsZWN0aW9ucy9jYXJkcy8zMi5wbmc.webp


if __name__ == '__main__':
    main()

```

\
Get NFT items by owner address:

```python
# Importing required package
from pytonapi import Tonapi


def main():
    # Creating new Tonapi object
    tonapi = Tonapi(api_key="Your api key")

    account_id = "EQC-3ilVr-W0Uc3pLrGJElwSaFxvhXXfkiQA3EwdVBHNNess"  # noqa
    result = tonapi.accounts.get_nfts(
        account_id=account_id, limit=10, offset=0
    )
    for nft in result.nft_items:
        # print nft address (raw)
        print(nft.address.to_raw())
        # output: 0:74c15fd0695c4706213ded4ac45eb7a2f87ff4c8f5d6bc904fe7dd1b735936e4

        # print nft address (userfriendly)
        print(nft.address.to_userfriendly())
        # output: EQB0wV_QaVxHBiE97UrEXrei-H_0yPXWvJBP590bc1k25KtT

        # print nft collection address
        print(nft.collection.address.to_userfriendly())
        # output: EQCA14o1-VWhS2efqoh_9M1b_A9DtKTuoqfmkn83AbJzwnPi

        # print nft previews url
        print(nft.previews[0].url)
        # output: https://cache.tonapi.io/imgproxy/c0wiqWVwr79OCcmR7qD-4WIKWOnk8t4vX_cqmohhE8s/rs:fill:100:100:1/g:no/aHR0cHM6Ly9uZnQudG9ubWVuZG9uLmNvbS9jb2xsZWN0aW9ucy9jYXJkcy8zMi5wbmc.webp


if __name__ == '__main__':
    main()

```

And more . . .\
\
\
**Donations:**\
<a href="https://app.tonkeeper.com/transfer/EQC-3ilVr-W0Uc3pLrGJElwSaFxvhXXfkiQA3EwdVBHNNess"><img src="https://telegra.ph//file/8e0ac22311be3fa6f772c.png" width="55"/></a>
<a href="https://tonhub.com/transfer/EQC-3ilVr-W0Uc3pLrGJElwSaFxvhXXfkiQA3EwdVBHNNess"><img src="https://telegra.ph//file/7fa75a1b454a00816d83b.png" width="55"/></a>\
```EQC-3ilVr-W0Uc3pLrGJElwSaFxvhXXfkiQA3EwdVBHNNess```
