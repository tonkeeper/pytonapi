from typing import List, Optional

from pydantic import BaseModel

from ._address import Address


class WalletStats(BaseModel):
    ton_balance: int
    nfts_count: int
    jettons_count: int
    multisig_count: int
    staking_count: int


class WalletPlugin(BaseModel):
    address: Address
    type: str


class Wallet(BaseModel):
    address: Address
    stats: WalletStats
    plugins: List[WalletPlugin]
    name: Optional[str] = None
    icon: Optional[str] = None
    is_suspended: Optional[bool] = None
