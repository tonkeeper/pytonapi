from __future__ import annotations

from enum import Enum

from pydantic import BaseModel

from .accounts import AccountAddress


class AccountStatus(str, Enum):
    nonexist = "nonexist"  # noqa
    uninit = "uninit"  # noqa
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
    cskip_no_state = "cskip_no_state"  # noqa
    cskip_bad_state = "cskip_bad_state"  # noqa
    cskip_no_gas = "cskip_no_gas"  # noqa


class AccStatusChange(str, Enum):
    acst_unchanged = "acst_unchanged"
    acst_frozen = "acst_frozen"
    acst_deleted = "acst_deleted"


class BouncePhaseType(str, Enum):
    TrPhaseBounceNegfunds = "TrPhaseBounceNegfunds"  # noqa
    TrPhaseBounceNofunds = "TrPhaseBounceNofunds"  # noqa
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
    fees_due: None | int
    status_change: AccStatusChange


class ComputePhase(BaseModel):
    skipped: bool
    skip_reason: None | ComputeSkipReason
    success: None | bool
    gas_fees: None | int
    gas_used: None | int
    vm_steps: None | int
    exit_code: None | int


class StateInit(BaseModel):
    code: None | str
    data: None | str
    library: dict[str, str]


class Message(BaseModel):
    created_lt: int
    ihr_disabled: bool
    bounce: bool
    bounced: bool
    value: int
    fwd_fee: int
    ihr_fee: int
    destination: None | AccountAddress
    source: None | AccountAddress
    import_fee: int
    created_at: int
    op_code: None | str
    init: None | StateInit
    decoded_op_name: None | str
    decoded_body: dict


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


class Trace(BaseModel):
    transaction: Transaction
    children: None | list[Trace]


class TraceId(BaseModel):
    id: str
    utime: int


class TraceIds(BaseModel):
    traces: list[TraceId]
