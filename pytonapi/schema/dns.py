from typing import List, Optional

from pydantic.v1 import BaseModel

from pytonapi.schema._address import Address


class WalletDNS(BaseModel):
    address: Address
    is_wallet: bool
    has_method_pubkey: bool
    has_method_seqno: bool
    names: List[str]


class DNSRecord(BaseModel):
    wallet: Optional[WalletDNS]
    next_resolver: Optional[str]
    sites: List[str]
    storage: Optional[str]


class Auction(BaseModel):
    domain: str
    owner: str
    price: int
    bids: int
    date: int


class Auctions(BaseModel):
    data: List[Auction]
    total: int
