from typing import List, Optional

from pydantic.v1 import BaseModel, Field


class BlockRaw(BaseModel):
    workchain: int
    shard: str
    seqno: int
    root_hash: str
    file_hash: str


class InitStateRaw(BaseModel):
    workchain: int
    root_hash: str
    file_hash: str


class RawMasterChainInfo(BaseModel):
    last: BlockRaw
    state_root_hash: str
    init: InitStateRaw


class RawMasterChainInfoExt(BaseModel):
    mode: int
    version: int
    capabilities: int
    last: BlockRaw
    last_utime: int
    now: int
    state_root_hash: str
    init: InitStateRaw


class RawGetBlock(BaseModel):
    id: BlockRaw
    data: str


class RawBlockState(BaseModel):
    id: BlockRaw
    root_hash: str
    file_hash: str
    data: str


class RawBlockHeader(BaseModel):
    id: BlockRaw
    mode: int
    header_proof: str


class RawAccountState(BaseModel):
    id: BlockRaw
    shardblk: BlockRaw
    shard_proof: str
    proof: str
    state: str


class RawShardInfo(BaseModel):
    id: BlockRaw
    shardblk: BlockRaw
    shard_proof: str
    shard_descr: str


class RawShardsInfo(BaseModel):
    id: BlockRaw
    proof: str
    data: str


class RawTransactions(BaseModel):
    ids: List[BlockRaw]
    transactions: str


class RawBlockTransactionID(BaseModel):
    mode: int
    account: Optional[str] = None
    lt: Optional[int] = None
    hash: Optional[str] = None


class RawListBlockTransactions(BaseModel):
    id: BlockRaw
    req_count: int
    incomplete: bool
    ids: List[RawBlockTransactionID]
    proof: str


class RawBlockProof(BaseModel):
    complete: bool
    from_: BlockRaw = Field(alias="from")
    to: BlockRaw
    steps: List


class RawConfig(BaseModel):
    mode: int
    id: BlockRaw
    state_proof: str
    config_proof: str


class RawShardProof(BaseModel):
    masterchain_id: BlockRaw
    links: List
