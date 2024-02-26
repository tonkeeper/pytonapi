from typing import List
from pydantic.v1 import BaseModel


class InscriptionBalance(BaseModel):
    type: str
    ticker: str
    balance: str
    decimals: int


class InscriptionBalances(BaseModel):
    inscriptions: List[InscriptionBalance]
