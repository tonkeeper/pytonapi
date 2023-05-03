from pydantic import BaseModel

from pytonapi.schema import Address, Balance


class Account(BaseModel):
    address: Address
    balance: Balance
    last_activity: int
    status: str
    interfaces: None | list[str]
    name: None | str
    is_scam: None | bool
    icon: None | str
    memo_required: None | bool
    get_methods: list[str]


class AccountAddress(BaseModel):
    address: Address
    name: None | str
    is_scam: bool
    icon: None | str
