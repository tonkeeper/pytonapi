from typing import List, Optional

from pydantic import BaseModel

from pytonapi.schema.accounts import AccountAddress


class Metadata(BaseModel):
    encrypted_binary: str
    decryption_key: Optional[str] = None


class CurrencyAmount(BaseModel):
    currency_type: str
    value: str
    decimals: int
    token_name: str
    verification: str
    image: str
    jetton: Optional[str] = None


class Purchase(BaseModel):
    event_id: str
    invoice_id: str
    source: AccountAddress
    destination: AccountAddress
    lt: int
    utime: int
    amount: CurrencyAmount
    metadata: Metadata


class Purchases(BaseModel):
    purchases: List[Purchase]
    next_from: int
