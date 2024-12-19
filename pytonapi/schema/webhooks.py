from typing import List, Optional

from pydantic import BaseModel


class WebhookCreate(BaseModel):
    webhook_id: int


class Webhook(BaseModel):
    id: int
    endpoint: str


class WebhookList(BaseModel):
    webhooks: List[Webhook]


class AccountSubscription(BaseModel):
    accounts: List[dict]


class AccountTxSubscription(BaseModel):
    account_id: str
    last_delivered_lt: int
    failed_at: Optional[str] = None
    failed_lt: Optional[int] = None
    failed_attempts: Optional[int] = None


class AccountSubscriptions(BaseModel):
    account_tx_subscriptions: List[AccountTxSubscription]
