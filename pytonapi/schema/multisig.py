from typing import List, Optional

from pydantic import BaseModel

from pytonapi.schema._address import Address
from pytonapi.schema.jettons import JettonQuantity
from pytonapi.schema.nft import NftItem


class Risk(BaseModel):
    description: Optional[str] = None
    transfer_all_remaining_balance: bool
    ton: int
    jettons: List[JettonQuantity]
    nfts: List[NftItem]


class MultisigOrder(BaseModel):
    address: Address
    order_seqno: int
    threshold: int
    sent_for_execution: bool
    signers: List[Address]
    approvals_num: int
    expiration_data: int
    risk: Risk


class Multisig(BaseModel):
    address: Address
    seqno: int
    threshold: int
    signers: List[Address]
    proposers: List[Address]
    orders: MultisigOrder


class Multisigs(BaseModel):
    multisigs: List[Multisig]
