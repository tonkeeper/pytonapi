from typing import Optional, List

from pydantic.v1 import BaseModel

from pytonapi.schema._address import Address
from pytonapi.schema._balance import Balance


class AddressFormB64(BaseModel):
    b64: str
    b64url: str


class AddressForm(BaseModel):
    raw_form: str
    bounceable: AddressFormB64
    non_bounceable: AddressFormB64
    given_type: str
    test_only: bool


class Account(BaseModel):
    address: Address
    balance: Balance
    last_activity: int
    status: str
    interfaces: Optional[List[str]]
    name: Optional[str]
    is_scam: Optional[bool]
    icon: Optional[str]
    memo_required: Optional[bool]
    get_methods: List[str]
    is_suspended: Optional[bool]
    is_wallet: bool


class Accounts(BaseModel):
    accounts: List[Account]


class AccountAddress(BaseModel):
    address: Address
    name: Optional[str]
    is_scam: bool
    icon: Optional[str]
    is_wallet: bool


class FoundAccount(BaseModel):
    address: Address
    name: Optional[str]
    preview: Optional[str]


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
    from pytonapi.schema.nft import NftItem
    expiring_at: int
    name: str
    dns_item: Optional[NftItem]


class DnsExpiring(BaseModel):
    items: List[DnsExpiringItemsInner]


class PublicKey(BaseModel):
    public_key: str


class BalanceChange(BaseModel):
    balance_change: Balance
