from __future__ import annotations

from typing import List, Optional, Dict, Any

from pydantic.v1 import BaseModel

from pytonapi.schema._address import Address
from pytonapi.schema.accounts import AccountAddress
from pytonapi.schema.traces import (
    AccountStatus,
    ActionPhase,
    BouncePhaseType,
    ComputePhase,
    CreditPhase,
    Message,
    StoragePhase,
    TransactionType,
)


class Transaction(BaseModel):
    hash: str
    lt: int
    account: AccountAddress
    success: bool
    utime: int
    orig_status: AccountStatus
    end_status: AccountStatus
    total_fees: int
    transaction_type: TransactionType
    state_update_old: str
    state_update_new: str
    in_msg: Optional[Message]
    out_msgs: List[Message]
    block: str
    prev_trans_hash: Optional[str]
    prev_trans_lt: Optional[int]
    compute_phase: Optional[ComputePhase]
    storage_phase: Optional[StoragePhase]
    credit_phase: Optional[CreditPhase]
    action_phase: Optional[ActionPhase]
    bounce_phase: Optional[BouncePhaseType]
    aborted: bool
    destroyed: bool


class Transactions(BaseModel):
    transactions: List[Transaction]


class Validator(BaseModel):
    address: Address


class Validators(BaseModel):
    validators: List[Validator]


class BlockchainBlock(BaseModel):
    workchain_id: int
    shard: str
    seqno: int
    root_hash: str
    file_hash: str
    global_id: int
    version: int
    after_merge: bool
    before_split: bool
    after_split: bool
    want_split: bool
    want_merge: bool
    key_block: bool
    gen_utime: int
    start_lt: int
    end_lt: int
    vert_seqno: int
    gen_catchain_seqno: int
    min_ref_mc_seqno: int
    prev_key_block_seqno: int
    gen_software_version: Optional[int]
    gen_software_capabilities: Optional[int]
    master_ref: Optional[str]
    prev_refs: List[str]
    in_msg_descr_length: int
    out_msg_descr_length: int
    rand_seed: str
    created_by: str


class BlockchainBlockShards(BaseModel):
    shards: List[Dict]


class RawBlockchainConfig(BaseModel):
    config: Dict[str, Any]


class AccountStorageInfo(BaseModel):
    used_cells: int
    used_bits: int
    used_public_cells: int
    last_paid: int
    due_payment: int


class BlockchainRawAccount(BaseModel):
    address: Address
    balance: int
    extra_balance: Optional[Dict[str, str]]
    code: Optional[str]
    data: Optional[str]
    last_transaction_lt: int
    status: str
    storage: AccountStorageInfo


class BlockchainAccountInspectMethodsInner(BaseModel):
    id: int
    method: str


class BlockchainAccountInspect(BaseModel):
    code: str
    code_hash: str
    methods: List[BlockchainAccountInspectMethodsInner]
    compiler: Optional[str]


class TvmStackRecord(BaseModel):
    type: str
    cell: Optional[str]
    slice: Optional[str]
    num: Optional[str]
    tuple: Optional[List[TvmStackRecord]]


class MethodExecutionResult(BaseModel):
    success: bool
    exit_code: int
    stack: List[TvmStackRecord]
    decoded: Optional[Any]
