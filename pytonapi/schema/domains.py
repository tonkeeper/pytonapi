from typing import List

from pydantic.v1 import BaseModel

from pytonapi.schema.accounts import AccountAddress


class DomainNames(BaseModel):
    domains: List[str]


class DomainBid(BaseModel):
    success: bool
    value: int
    txTime: int
    txHash: str
    bidder: AccountAddress


class DomainBids(BaseModel):
    data: List[DomainBid]
