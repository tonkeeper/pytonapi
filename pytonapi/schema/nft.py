from typing import List, Optional

from pydantic.v1 import BaseModel

from pytonapi.schema._address import Address
from pytonapi.schema.accounts import AccountAddress


class Price(BaseModel):
    value: str
    token_name: str


class Sale(BaseModel):
    address: Address
    market: AccountAddress
    owner: Optional[AccountAddress]
    price: Price


class ImagePreview(BaseModel):
    resolution: str
    url: str


class Collection(BaseModel):
    address: Address
    name: str
    description: Optional[str]


class NftCollection(BaseModel):
    address: Address
    next_item_index: int
    owner: Optional[AccountAddress]
    raw_collection_content: str
    metadata: Optional[dict]
    previews: Optional[List[ImagePreview]]


class NftItem(BaseModel):
    address: Address
    index: int
    owner: Optional[AccountAddress]
    collection: Optional[Collection]
    verified: bool
    metadata: dict
    sale: Optional[Sale]
    previews: Optional[List[ImagePreview]]
    dns: Optional[str]
    approved_by: List[str]


class NftItems(BaseModel):
    nft_items: List[NftItem]


class NftCollections(BaseModel):
    nft_collections: List[NftCollection]
