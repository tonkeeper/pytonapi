from typing import List, Optional

from pydantic import BaseModel, Field


class GaslessJetton(BaseModel):
    master_id: str


class GaslessConfig(BaseModel):
    relay_address: str
    gas_jettons: List[GaslessJetton]


class SignRawMessage(BaseModel):
    address: str
    amount: str
    payload: Optional[str] = None
    stateInit: Optional[str] = None


class SignRawParams(BaseModel):
    relay_address: str
    commission: str
    from_: str = Field(alias="from")
    valid_until: int
    messages: List[SignRawMessage]
