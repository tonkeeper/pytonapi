from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import BaseModel

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
    result_code: int
    total_actions: int
    skipped_actions: int
    fwd_fees: int
    total_fees: int
    result_code_description: Optional[str] = None


class CreditPhase(BaseModel):
    fees_collected: int
    credit: int


class StoragePhase(BaseModel):
    fees_collected: int
    fees_due: Optional[int] = None
    status_change: AccStatusChange


class ComputePhase(BaseModel):
    skipped: bool
    skip_reason: Optional[ComputeSkipReason] = None
    success: Optional[bool] = None
    gas_fees: Optional[int] = None
    gas_used: Optional[int] = None
    vm_steps: Optional[int] = None
    exit_code: Optional[int] = None
    exit_code_description: Optional[int] = None


class StateInit(BaseModel):
    boc: str


class Message(BaseModel):
    msg_type: str
    created_lt: int
    ihr_disabled: bool
    bounce: bool
    bounced: bool
    value: int
    value_extra: Optional[int] = None
    fwd_fee: int
    ihr_fee: int
    destination: Optional[AccountAddress] = None
    source: Optional[AccountAddress] = None
    import_fee: int
    created_at: int
    op_code: Optional[str] = None
    init: Optional[StateInit] = None
    decoded_op_name: Optional[str] = None
    decoded_body: Optional[Union[dict, str]] = None
    hash: Optional[str] = None
    raw_body: Optional[str] = None


class Transaction(BaseModel):
    hash: str
    lt: int
    account: AccountAddress
    success: bool
    utime: int
    orig_status: AccountStatus
    end_status: AccountStatus
    total_fees: int
    end_balance: int
    transaction_type: TransactionType
    state_update_old: str
    state_update_new: str
    in_msg: Optional[Message] = None
    out_msgs: List[Message]
    block: str
    prev_trans_hash: Optional[str] = None
    prev_trans_lt: Optional[int] = None
    compute_phase: Optional[ComputePhase] = None
    storage_phase: Optional[StoragePhase] = None
    credit_phase: Optional[CreditPhase] = None
    action_phase: Optional[ActionPhase] = None
    bounce_phase: Optional[BouncePhaseType] = None
    aborted: bool
    destroyed: bool
    raw: str


class Trace(BaseModel):
    transaction: Transaction
    interfaces: Optional[List[str]] = None
    children: Optional[List[Trace]] = None
    emulated: Optional[bool] = None


class TraceId(BaseModel):
    id: str
    utime: int


class TraceIds(BaseModel):
    traces: List[TraceId]
