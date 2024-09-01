from enum import Enum
from typing import Any, List, Optional

from pydantic import BaseModel

from pytonapi.schema._address import Address
from pytonapi.schema.accounts import AccountAddress


class Price(BaseModel):
    value: str
    token_name: str


class Sale(BaseModel):
    address: Address
    market: AccountAddress
    owner: Optional[AccountAddress] = None
    price: Price


class ImagePreview(BaseModel):
    resolution: str
    url: str


class Collection(BaseModel):
    address: Address
    name: str
    description: Optional[str] = None


class NftApprovedBy(str, Enum):
    getgems = "getgems"
    tonkeeper = "tonkeeper"
    ton_diamonds = "ton.diamonds"
    none = "none"

    @classmethod
    def _missing_(cls, value: Any) -> str:
        return cls.none


class NftCollection(BaseModel):
    address: Address
    next_item_index: int
    owner: Optional[AccountAddress] = None
    raw_collection_content: str
    metadata: Optional[dict] = None
    previews: Optional[List[ImagePreview]] = None
    approved_by: NftApprovedBy


class TrustType(str, Enum):
    whitelist = "whitelist"
    graylist = "graylist"
    blacklist = "blacklist"
    none = "none"

    @classmethod
    def _missing_(cls, value: Any) -> str:
        return cls.none


class NftItem(BaseModel):
    address: Address
    index: int
    owner: Optional[AccountAddress] = None
    collection: Optional[Collection] = None
    verified: bool
    metadata: dict
    sale: Optional[Sale] = None
    previews: Optional[List[ImagePreview]] = None
    dns: Optional[str] = None
    approved_by: List[str]
    include_cnft: Optional[bool] = None
    trust: TrustType


class NftItems(BaseModel):
    nft_items: List[NftItem]


class NftCollections(BaseModel):
    nft_collections: List[NftCollection]
