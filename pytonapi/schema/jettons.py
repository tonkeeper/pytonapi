from enum import Enum
from typing import List, Optional

from pydantic.v1 import BaseModel

from pytonapi.schema._address import Address
from pytonapi.schema.accounts import AccountAddress
from pytonapi.schema.rates import TokenRates


class JettonVerificationType(str, Enum):
    whitelist = "whitelist"
    blacklist = "blacklist"
    none = "none"


class JettonMetadata(BaseModel):
    address: Address
    name: str
    symbol: str
    decimals: str
    image: Optional[str]
    description: Optional[str]
    social: Optional[List[str]]
    websites: Optional[List[str]]
    catalogs: Optional[List[str]]


class JettonInfo(BaseModel):
    mintable: bool
    total_supply: str
    metadata: JettonMetadata
    verification: JettonVerificationType
    holders_count: int


class JettonPreview(BaseModel):
    address: Address
    name: str
    symbol: str
    decimals: int
    image: str
    verification: JettonVerificationType


class JettonBalance(BaseModel):
    balance: str
    price: Optional[TokenRates]
    wallet_address: AccountAddress
    jetton: JettonPreview


class JettonsBalances(BaseModel):
    balances: List[JettonBalance]


class JettonHolder(BaseModel):
    address: Address
    owner: AccountAddress
    balance: str


class JettonHolders(BaseModel):
    addresses: List[JettonHolder]
    total: int


class Jettons(BaseModel):
    jettons: List[JettonInfo]


class JettonQuantity(BaseModel):
    quantity: str
    wallet_address: AccountAddress
    jetton: JettonPreview
