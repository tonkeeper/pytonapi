from enum import Enum
from typing import Any, List, Optional

from pydantic import BaseModel

from pytonapi.schema._address import Address
from pytonapi.schema.accounts import AccountAddress
from pytonapi.schema.rates import TokenRates


class JettonVerificationType(str, Enum):
    whitelist = "whitelist"
    graylist = "graylist"
    blacklist = "blacklist"
    none = "none"

    @classmethod
    def _missing_(cls, value: Any) -> str:
        return cls.none


class JettonMetadata(BaseModel):
    address: Address
    name: str
    symbol: str
    decimals: str
    image: Optional[str] = None
    description: Optional[str] = None
    social: Optional[List[str]] = None
    websites: Optional[List[str]] = None
    catalogs: Optional[List[str]] = None


class JettonInfo(BaseModel):
    mintable: bool
    total_supply: str
    admin: Optional[AccountAddress] = None
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
    custom_payload_api_uri: Optional[str] = None
    score: int


class JettonBalance(BaseModel):
    balance: str
    price: Optional[TokenRates] = None
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


class JettonTransferPayload(BaseModel):
    custom_payload: Optional[str] = None
    state_init: Optional[str] = None


class JettonOperation(BaseModel):
    operation: str
    utime: int
    lt: int
    transaction_hash: str
    source: Optional[AccountAddress] = None
    destination: Optional[AccountAddress] = None
    amount: str
    jetton: JettonPreview
    trace_id: str
    query_id: str
    payload: Optional[Any]


class JettonOperations(BaseModel):
    operations: List[JettonOperation]
    next_form: Optional[int] = None
