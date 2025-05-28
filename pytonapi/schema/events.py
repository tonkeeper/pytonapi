from typing import List, Optional

from pydantic import BaseModel

from pytonapi.schema._address import Address
from pytonapi.schema.accounts import AccountAddress
from pytonapi.schema.jettons import JettonPreview, JettonQuantity
from pytonapi.schema.nft import NftItem, Price
from pytonapi.schema.traces import Trace


class Refund(BaseModel):
    type: str
    origin: str


class EncryptedComment(BaseModel):
    encryption_type: str
    cipher_text: str


class TonTransferAction(BaseModel):
    sender: AccountAddress
    recipient: AccountAddress
    amount: int
    comment: Optional[str] = None
    encrypted_comment: Optional[EncryptedComment] = None
    refund: Optional[Refund] = None


class ContractDeployAction(BaseModel):
    address: Address
    interfaces: List[str]


class JettonTransferAction(BaseModel):
    sender: Optional[AccountAddress] = None
    recipient: Optional[AccountAddress] = None
    senders_wallet: str
    recipients_wallet: str
    amount: str
    comment: Optional[str] = None
    encrypted_comment: Optional[EncryptedComment] = None
    refund: Optional[Refund] = None
    jetton: JettonPreview


class JettonBurnAction(BaseModel):
    sender: AccountAddress
    senders_wallet: str
    amount: str
    jetton: JettonPreview


class JettonMintAction(BaseModel):
    recipient: AccountAddress
    recipients_wallet: str
    amount: str
    jetton: JettonPreview


class NftItemTransferAction(BaseModel):
    sender: Optional[AccountAddress] = None
    recipient: Optional[AccountAddress] = None
    nft: str
    comment: Optional[str] = None
    encrypted_comment: Optional[EncryptedComment] = None
    payload: Optional[str] = None
    refund: Optional[Refund] = None


class SubscriptionAction(BaseModel):
    subscriber: AccountAddress
    subscription: str
    beneficiary: AccountAddress
    amount: int
    initial: bool


class UnSubscriptionAction(BaseModel):
    subscriber: AccountAddress
    subscription: str
    beneficiary: AccountAddress


class AuctionBidAction(BaseModel):
    auction_type: str
    amount: Price
    nft: Optional[NftItem] = None
    bidder: AccountAddress
    auction: AccountAddress


class NftPurchaseAction(BaseModel):
    auction_type: str
    amount: Price
    nft: NftItem
    seller: AccountAddress
    buyer: AccountAddress


class DepositStakeAction(BaseModel):
    amount: int
    staker: AccountAddress
    pool: AccountAddress


class WithdrawStakeAction(BaseModel):
    amount: int
    staker: AccountAddress
    pool: AccountAddress


class WithdrawStakeRequestAction(BaseModel):
    amount: Optional[int] = None
    staker: AccountAddress
    pool: AccountAddress


class ElectionsDepositStakeAction(BaseModel):
    amount: int
    staker: AccountAddress


class ElectionsRecoverStakeAction(BaseModel):
    amount: int
    staker: AccountAddress


class JettonSwapAction(BaseModel):
    dex: str
    amount_in: str
    amount_out: str
    ton_in: Optional[int] = None
    ton_out: Optional[int] = None
    user_wallet: AccountAddress
    router: AccountAddress
    jetton_master_in: Optional[JettonPreview] = None
    jetton_master_out: Optional[JettonPreview] = None


class SmartContractAction(BaseModel):
    executor: AccountAddress
    contract: AccountAddress
    ton_attached: int
    operation: str
    payload: Optional[str] = None
    refund: Optional[Refund] = None


class ActionSimplePreview(BaseModel):
    name: str
    description: str
    action_image: Optional[str] = None
    value: Optional[str] = None
    value_image: Optional[str] = None
    accounts: List[AccountAddress]


class DomainRenewAction(BaseModel):
    domain: str
    contract_address: Address
    renewer: AccountAddress


class InscriptionTransferAction(BaseModel):
    sender: AccountAddress
    recipient: AccountAddress
    amount: str
    comment: Optional[str] = None
    type: str
    ticker: str
    decimals: int


class InscriptionMintAction(BaseModel):
    recipient: AccountAddress
    amount: str
    type: str
    ticker: str
    decimals: int


class Action(BaseModel):
    type: str
    status: str
    TonTransfer: Optional[TonTransferAction] = None
    ContractDeploy: Optional[ContractDeployAction] = None
    JettonTransfer: Optional[JettonTransferAction] = None
    JettonBurn: Optional[JettonBurnAction] = None
    JettonMint: Optional[JettonMintAction] = None
    NftItemTransfer: Optional[NftItemTransferAction] = None
    Subscribe: Optional[SubscriptionAction] = None
    UnSubscribe: Optional[UnSubscriptionAction] = None
    AuctionBid: Optional[AuctionBidAction] = None
    NftPurchase: Optional[NftPurchaseAction] = None
    DepositStake: Optional[DepositStakeAction] = None
    WithdrawStake: Optional[WithdrawStakeAction] = None
    WithdrawStakeRequest: Optional[WithdrawStakeRequestAction] = None
    ElectionsDepositStake: Optional[ElectionsDepositStakeAction] = None
    ElectionsRecoverStake: Optional[ElectionsRecoverStakeAction] = None
    JettonSwap: Optional[JettonSwapAction] = None
    SmartContractExec: Optional[SmartContractAction] = None
    DomainRenew: Optional[DomainRenewAction] = None
    InscriptionTransfer: Optional[InscriptionTransferAction] = None
    InscriptionMint: Optional[InscriptionMintAction] = None
    simple_preview: ActionSimplePreview


class AccountEvent(BaseModel):
    event_id: str
    account: AccountAddress
    timestamp: int
    actions: List[Action]
    is_scam: bool
    lt: int
    in_progress: bool
    extra: int


class AccountEvents(BaseModel):
    events: List[AccountEvent]
    next_from: int


class ValueFlowJettonsInner(BaseModel):
    account: AccountAddress
    jetton: JettonPreview
    quantity: int


class ValueFlow(BaseModel):
    account: AccountAddress
    ton: int
    fees: int
    jettons: Optional[List[ValueFlowJettonsInner]] = None


class Event(BaseModel):
    event_id: str
    timestamp: int
    actions: List[Action]
    value_flow: List[ValueFlow]
    is_scam: bool
    lt: int
    in_progress: bool


class MempoolEventData(BaseModel):
    boc: str


class TraceEventData(BaseModel):
    accounts: List[Address]
    hash: str


class TransactionEventData(BaseModel):
    account_id: Address
    lt: int
    tx_hash: str


class BlockEventData(BaseModel):
    workchain: int
    shard: str
    seqno: int
    root_hash: str
    file_hash: str


class Risk(BaseModel):
    description: Optional[str] = None
    transfer_all_remaining_balance: bool
    ton: int
    jettons: List[JettonQuantity]
    nfts: List[NftItem]


class MessageConsequences(BaseModel):
    trace: Trace
    risk: Risk
    event: AccountEvent
