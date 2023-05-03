from pydantic import BaseModel

from pytonapi.schema.accounts import AccountAddress

from pytonapi.schema.traces import (Message, AccountStatus, TransactionType,
                                    ComputePhase, StoragePhase, CreditPhase, ActionPhase, BouncePhaseType)


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
    gen_software_version: None | int
    gen_software_capabilities: None | int
    master_ref: None | str
    prev_refs: list[str]
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
    in_msg: None | Message
    out_msgs: list[Message]
    block: str
    prev_trans_hash: None | str
    prev_trans_lt: None | int
    compute_phase: None | ComputePhase
    storage_phase: None | StoragePhase
    credit_phase: None | CreditPhase
    action_phase: None | ActionPhase
    bounce_phase: None | BouncePhaseType
    aborted: bool
    destroyed: bool


class Transactions(BaseModel):
    transactions: list[Transaction]


