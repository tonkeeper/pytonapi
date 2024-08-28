from typing import List, Optional

from pydantic import BaseModel

from pytonapi.schema.accounts import AccountAddress
from pytonapi.schema.nft import NftItem


class DomainNames(BaseModel):
    domains: List[str]


class DomainInfo(BaseModel):
    name: str
    expiring_at: Optional[int] = None
    item: Optional[NftItem] = None


class DomainBid(BaseModel):
    success: bool
    value: int
    txTime: int
    txHash: str
    bidder: AccountAddress


class DomainBids(BaseModel):
    data: List[DomainBid]
