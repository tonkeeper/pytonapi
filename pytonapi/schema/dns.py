from pydantic import BaseModel

from pytonapi.schema import Address


class WalletDNS(BaseModel):
    address: Address
    is_wallet: bool
    has_method_pubkey: bool
    has_method_seqno: bool
    names: list[str]


class DNSRecord(BaseModel):
    wallet: None | WalletDNS
    next_resolver: None | str
    sites: list[str]
    storage: None | str
