from pydantic import BaseModel

from . import Address
from .accounts import AccountAddress


class Price(BaseModel):
    value: str
    token_name: str


class Sale(BaseModel):
    address: Address
    market: AccountAddress
    owner: None | AccountAddress
    price: Price


class ImagePreview(BaseModel):
    resolution: str
    url: str


class Collection(BaseModel):
    address: Address
    name: str


class NftCollection(BaseModel):
    address: Address
    next_item_index: int
    owner: AccountAddress
    raw_collection_content: str
    metadata: None | dict


class NftItem(BaseModel):
    address: Address
    index: int
    owner: None | AccountAddress
    collection: None | Collection
    verified: bool
    metadata: dict
    sale: None | Sale
    previews: None | list[ImagePreview]
    dns: None | str
    approved_by: list[str]


class NftItems(BaseModel):
    nft_items: list[NftItem]


class NftCollections(BaseModel):
    nft_collections: list[NftCollection]
