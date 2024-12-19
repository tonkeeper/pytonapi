from typing import Optional, List

from pydantic import BaseModel

from pytonapi.schema._address import Address
from pytonapi.schema._balance import Balance


class Account(BaseModel):
    address: Address
    balance: Balance
    last_activity: int
    status: str
    interfaces: Optional[List[str]] = None
    name: Optional[str] = None
    is_scam: Optional[bool] = None
    icon: Optional[str] = None
    memo_required: Optional[bool] = None
    get_methods: List[str]
    is_suspended: Optional[bool] = None
    is_wallet: bool


class Accounts(BaseModel):
    accounts: List[Account]


class AccountAddress(BaseModel):
    address: Address
    name: Optional[str] = None
    is_scam: bool
    icon: Optional[str] = None
    is_wallet: bool


class FoundAccount(BaseModel):
    address: Address
    name: Optional[str] = None
    preview: Optional[str] = None


class FoundAccounts(BaseModel):
    addresses: List[FoundAccount]


class Subscription(BaseModel):
    address: Address
    wallet_address: Address
    beneficiary_address: Address
    amount: Balance
    period: int
    start_time: int
    timeout: int
    last_payment_time: int
    last_request_time: int
    subscription_id: int
    failed_attempts: int


class Subscriptions(BaseModel):
    subscriptions: List[Subscription]


class DnsExpiringItemsInner(BaseModel):
    expiring_at: int
    name: str
    dns_item: Optional["NftItem"] = None


class DnsExpiring(BaseModel):
    items: List[DnsExpiringItemsInner]


class PublicKey(BaseModel):
    public_key: str


class BalanceChange(BaseModel):
    balance_change: Balance


from pytonapi.schema.nft import NftItem
