from typing import List, Optional

from pydantic.v1 import BaseModel

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
    comment: Optional[str]
    encrypted_comment: Optional[EncryptedComment]
    refund: Optional[Refund]


class ContractDeployAction(BaseModel):
    address: Address
    interfaces: List[str]


class JettonTransferAction(BaseModel):
    sender: Optional[AccountAddress]
    recipient: Optional[AccountAddress]
    senders_wallet: str
    recipients_wallet: str
    amount: str
    comment: Optional[str]
    encrypted_comment: Optional[EncryptedComment]
    refund: Optional[Refund]
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
    sender: Optional[AccountAddress]
    recipient: Optional[AccountAddress]
    nft: str
    comment: Optional[str]
    encrypted_comment: Optional[EncryptedComment]
    payload: Optional[str]
    refund: Optional[Refund]


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
    nft: Optional[NftItem]
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
    amount: Optional[int]
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
    ton_in: Optional[int]
    ton_out: Optional[int]
    user_wallet: AccountAddress
    router: AccountAddress
    jetton_master_in: Optional[JettonPreview]
    jetton_master_out: Optional[JettonPreview]


class SmartContractAction(BaseModel):
    executor: AccountAddress
    contract: AccountAddress
    ton_attached: int
    operation: str
    payload: Optional[str]
    refund: Optional[Refund]


class ActionSimplePreview(BaseModel):
    name: str
    description: str
    action_image: Optional[str]
    value: Optional[str]
    value_image: Optional[str]
    accounts: List[AccountAddress]


class DomainRenewAction(BaseModel):
    domain: str
    contract_address: Address
    renewer: AccountAddress


class InscriptionTransferAction(BaseModel):
    sender: AccountAddress
    recipient: AccountAddress
    amount: str
    comment: Optional[str]
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
    TonTransfer: Optional[TonTransferAction]
    ContractDeploy: Optional[ContractDeployAction]
    JettonTransfer: Optional[JettonTransferAction]
    JettonBurn: Optional[JettonBurnAction]
    JettonMint: Optional[JettonMintAction]
    NftItemTransfer: Optional[NftItemTransferAction]
    Subscribe: Optional[SubscriptionAction]
    UnSubscribe: Optional[UnSubscriptionAction]
    AuctionBid: Optional[AuctionBidAction]
    NftPurchase: Optional[NftPurchaseAction]
    DepositStake: Optional[DepositStakeAction]
    WithdrawStake: Optional[WithdrawStakeAction]
    WithdrawStakeRequest: Optional[WithdrawStakeRequestAction]
    ElectionsDepositStake: Optional[ElectionsDepositStakeAction]
    ElectionsRecoverStake: Optional[ElectionsRecoverStakeAction]
    JettonSwap: Optional[JettonSwapAction]
    SmartContractExec: Optional[SmartContractAction]
    DomainRenew: Optional[DomainRenewAction]
    InscriptionTransfer: Optional[InscriptionTransferAction]
    InscriptionMint: Optional[InscriptionMintAction]
    simple_preview: ActionSimplePreview


class AccountEvent(BaseModel):
    description: Optional[str]
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
    quantity: int


class ValueFlow(BaseModel):
    account: AccountAddress
    ton: int
    fees: int
    jettons: Optional[List[ValueFlowJettonsInner]]


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
