from typing import Optional, List

from pydantic import BaseModel

from pytonapi.schema._address import Address
from pytonapi.schema._balance import Balance


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


class Accounts(BaseModel):
    accounts: List[Account]


class AccountAddress(BaseModel):
    address: Address
    name: Optional[str]
    is_scam: bool
    icon: Optional[str]
