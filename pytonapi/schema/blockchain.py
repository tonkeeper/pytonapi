from __future__ import annotations

from typing import List, Optional, Dict, Any

from pydantic.v1 import BaseModel, Field

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
    adnl_address: str
    stake: int
    max_factor: int


class Validators(BaseModel):
    elect_at: int
    elect_close: int
    min_stake: int
    total_stake: int
    validators: List[Validator]


class ValidatorSet(BaseModel):
    utime_since: int
    utime_until: int
    total: int
    main: int
    total_weight: Optional[int] = None
    list: List


class BlockCurrencyCollection(BaseModel):
    grams: int
    other: List[Dict[str, Any]]


class BlockValueFlow(BaseModel):
    from_prev_blk: BlockCurrencyCollection
    to_next_blk: BlockCurrencyCollection
    imported: BlockCurrencyCollection
    exported: BlockCurrencyCollection
    fees_collected: BlockCurrencyCollection
    burned: Optional[BlockCurrencyCollection]
    fees_imported: BlockCurrencyCollection
    recovered: BlockCurrencyCollection
    created: BlockCurrencyCollection
    minted: BlockCurrencyCollection


class BlockchainBlock(BaseModel):
    tx_quantity: int
    value_flow: BlockValueFlow
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


class BlockchainBlocks(BaseModel):
    blocks: List[BlockchainBlock]


class BlockchainBlockShards(BaseModel):
    shards: List[Dict[str, Any]]


class RawBlockchainConfig(BaseModel):
    config: Dict[str, Any]


class BlockchainConfig(BaseModel):
    c0: str = Field(alias="0")
    c1: str = Field(alias="1")
    c2: str = Field(alias="2")
    c3: Optional[str] = Field(alias="3", default=None)
    c4: str = Field(alias="4")
    c5: Optional[Dict[str, Any]] = Field(alias="5", default=None)
    c6: Optional[Dict[str, Any]] = Field(alias="6", default=None)
    c7: Optional[Dict[str, Any]] = Field(alias="7", default=None)
    c8: Optional[Dict[str, Any]] = Field(alias="8", default=None)
    c9: Optional[Dict[str, Any]] = Field(alias="9", default=None)
    c10: Optional[Dict[str, Any]] = Field(alias="10", default=None)
    c11: Optional[Dict[str, Any]] = Field(alias="11", default=None)
    c12: Optional[Dict[str, Any]] = Field(alias="12", default=None)
    c13: Optional[Dict[str, Any]] = Field(alias="13", default=None)
    c14: Optional[Dict[str, Any]] = Field(alias="14", default=None)
    c15: Optional[Dict[str, Any]] = Field(alias="15", default=None)
    c16: Optional[Dict[str, Any]] = Field(alias="16", default=None)
    c17: Optional[Dict[str, Any]] = Field(alias="17", default=None)
    c18: Optional[Dict[str, Any]] = Field(alias="18", default=None)
    c19: Optional[Dict[str, Any]] = Field(alias="19", default=None)
    c20: Optional[Dict[str, Any]] = Field(alias="20", default=None)
    c21: Optional[Dict[str, Any]] = Field(alias="21", default=None)
    c22: Optional[Dict[str, Any]] = Field(alias="22", default=None)
    c23: Optional[Dict[str, Any]] = Field(alias="23", default=None)
    c24: Optional[Dict[str, Any]] = Field(alias="24", default=None)
    c25: Optional[Dict[str, Any]] = Field(alias="25", default=None)
    c26: Optional[Dict[str, Any]] = Field(alias="26", default=None)
    c27: Optional[Dict[str, Any]] = Field(alias="27", default=None)
    c28: Optional[Dict[str, Any]] = Field(alias="28", default=None)
    c29: Optional[Dict[str, Any]] = Field(alias="29", default=None)
    c30: Optional[Dict[str, Any]] = Field(alias="30", default=None)
    c31: Optional[Dict[str, Any]] = Field(alias="31", default=None)
    c32: Optional[ValidatorSet] = Field(alias="32", default=None)
    c33: Optional[ValidatorSet] = Field(alias="33", default=None)
    c34: Optional[ValidatorSet] = Field(alias="34", default=None)
    c35: Optional[ValidatorSet] = Field(alias="35", default=None)
    c36: Optional[ValidatorSet] = Field(alias="36", default=None)
    c37: Optional[ValidatorSet] = Field(alias="37", default=None)
    c38: Optional[Dict[str, Any]] = Field(alias="38", default=None)
    c39: Optional[Dict[str, Any]] = Field(alias="39", default=None)
    c40: Optional[Dict[str, Any]] = Field(alias="40", default=None)
    c41: Optional[Dict[str, Any]] = Field(alias="41", default=None)
    c42: Optional[Dict[str, Any]] = Field(alias="42", default=None)
    c43: Optional[Dict[str, Any]] = Field(alias="43", default=None)
    c44: Optional[Dict[str, Any]] = Field(alias="44", default=None)
    c71: Optional[Dict[str, Any]] = Field(alias="71", default=None)
    c72: Optional[Dict[str, Any]] = Field(alias="72", default=None)
    c73: Optional[Dict[str, Any]] = Field(alias="73", default=None)
    c79: Optional[Dict[str, Any]] = Field(alias="79", default=None)
    c81: Optional[Dict[str, Any]] = Field(alias="81", default=None)
    c82: Optional[Dict[str, Any]] = Field(alias="82", default=None)
    raw: str


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
    last_transaction_hash: Optional[str]
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


class ServiceStatus(BaseModel):
    rest_online: bool
    indexing_latency: int


class DecodedMessage(BaseModel):
    destination: AccountAddress
    destination_wallet_version: str
    ext_in_msg_decoded: Optional[Dict[str, Any]]
