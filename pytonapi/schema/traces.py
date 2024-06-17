from __future__ import annotations

from enum import Enum
from typing import Optional, List, Union

from pydantic.v1 import BaseModel

from .accounts import AccountAddress


class AccountStatus(str, Enum):
    nonexist = "nonexist"
    uninit = "uninit"
    active = "active"
    frozen = "frozen"


class TransactionType(str, Enum):
    TransOrd = "TransOrd"
    TransTickTock = "TransTickTock"
    TransSplitPrepare = "TransSplitPrepare"
    TransSplitInstall = "TransSplitInstall"
    TransMergePrepare = "TransMergePrepare"
    TransMergeInstall = "TransMergeInstall"
    TransStorage = "TransStorage"


class ComputeSkipReason(str, Enum):
    cskip_no_state = "cskip_no_state"
    cskip_bad_state = "cskip_bad_state"
    cskip_no_gas = "cskip_no_gas"


class AccStatusChange(str, Enum):
    acst_unchanged = "acst_unchanged"
    acst_frozen = "acst_frozen"
    acst_deleted = "acst_deleted"


class BouncePhaseType(str, Enum):
    TrPhaseBounceNegfunds = "TrPhaseBounceNegfunds"
    TrPhaseBounceNofunds = "TrPhaseBounceNofunds"
    TrPhaseBounceOk = "TrPhaseBounceOk"


class ActionPhase(BaseModel):
    success: bool
    total_actions: int
    skipped_actions: int
    fwd_fees: int
    total_fees: int


class CreditPhase(BaseModel):
    fees_collected: int
    credit: int


class StoragePhase(BaseModel):
    fees_collected: int
    fees_due: Optional[int]
    status_change: AccStatusChange


class ComputePhase(BaseModel):
    skipped: bool
    skip_reason: Optional[ComputeSkipReason]
    success: Optional[bool]
    gas_fees: Optional[int]
    gas_used: Optional[int]
    vm_steps: Optional[int]
    exit_code: Optional[int]


class StateInit(BaseModel):
    boc: str


class Message(BaseModel):
    created_lt: int
    ihr_disabled: bool
    bounce: bool
    bounced: bool
    value: int
    fwd_fee: int
    ihr_fee: int
    destination: Optional[AccountAddress]
    source: Optional[AccountAddress]
    import_fee: int
    created_at: int
    op_code: Optional[str]
    init: Optional[StateInit]
    decoded_op_name: Optional[str]
    decoded_body: Optional[Union[dict, str]]
    raw_body: Optional[str]


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


class Trace(BaseModel):
    transaction: Transaction
    interfaces: Optional[List[str]]
    children: Optional[List[Trace]]
    emulated: Optional[bool]


class TraceId(BaseModel):
    id: str
    utime: int


class TraceIds(BaseModel):
    traces: List[TraceId]
