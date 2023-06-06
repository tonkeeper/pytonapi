from typing import List, Optional

from pydantic import BaseModel

from pytonapi.schema.accounts import AccountAddress
from pytonapi.schema.traces import (AccountStatus, TransactionType,
                                    BouncePhaseType, ActionPhase,
                                    CreditPhase, StoragePhase,
                                    ComputePhase, Message)


class Block(BaseModel):
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
