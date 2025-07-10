from typing import List, Optional

from pydantic import BaseModel

from ._address import Address


class WalletStats(BaseModel):
    nfts_count: int
    jettons_count: int
    multisig_count: int
    staking_count: int


class WalletPlugin(BaseModel):
    address: Address
    type: str


class Wallet(BaseModel):
    address: Address
    is_wallet: bool
    balance: int
    stats: WalletStats
    status: str
    last_activity: int
    plugins: List[WalletPlugin]
    name: Optional[str] = None
    icon: Optional[str] = None
    is_suspended: Optional[bool] = None
    signature_disabled: bool
    interfaces: List[str]
    last_lt: int
