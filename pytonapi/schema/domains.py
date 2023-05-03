from pydantic import BaseModel

from pytonapi.schema.accounts import AccountAddress


class DomainNames(BaseModel):
    domains: list[str]


class DomainBid(BaseModel):
    success: bool
    value: int
    txTime: int
    txHash: str
    bidder: AccountAddress


class DomainBids(BaseModel):
    data: list[DomainBid]
