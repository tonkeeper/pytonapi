from typing import List

from pydantic.v1 import BaseModel

from pytonapi.schema._address import Address


class StorageProvider(BaseModel):
    address: Address
    accept_new_contracts: bool
    rate_per_mb_day: int
    max_span: int
    minimal_file_size: int
    maximal_file_size: int


class StorageProviders(BaseModel):
    providers: List[StorageProvider]
