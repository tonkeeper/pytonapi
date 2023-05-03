from enum import Enum

from pydantic import BaseModel

from . import Address
from .accounts import AccountAddress


class JettonVerificationType(Enum):
    whitelist: str = "whitelist"
    blacklist: str = "blacklist"
    none: str = "none"


class JettonMetadata(BaseModel):
    address: Address
    name: str
    symbol: str
    decimals: str
    image: None | str
    description: None | str
    social: None | list[str]
    websites: None | list[str]
    catalogs: None | list[str]


class JettonInfo(BaseModel):
    mintable: bool
    total_supply: str
    metadata: JettonMetadata
    verification: JettonVerificationType


class JettonPreview(BaseModel):
    address: Address
    name: str
    symbol: str
    decimals: int
    image: str
    verification: JettonVerificationType


class JettonBalance(BaseModel):
    balance: str
    wallet_address: AccountAddress
    jetton: JettonPreview


class JettonsBalances(BaseModel):
    balances: list[JettonBalance]
