from typing import List, Optional

from pydantic.v1 import BaseModel

from pytonapi.schema.accounts import AccountAddress
from pytonapi.schema.nft import NftItem


class DomainNames(BaseModel):
    domains: List[str]


class DomainInfo(BaseModel):
    name: str
    expiring_at: Optional[int]
    item: Optional[NftItem]


class DomainBid(BaseModel):
    success: bool
    value: int
    txTime: int
    txHash: str
    bidder: AccountAddress


class DomainBids(BaseModel):
    data: List[DomainBid]
