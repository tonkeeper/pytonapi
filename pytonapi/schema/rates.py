from typing import Dict, Any, Optional

from pydantic.v1 import BaseModel


class Rates(BaseModel):
    rates: Dict[str, Dict]


class ChartRates(BaseModel):
    points: Dict[str, Any]


class TokenRates(BaseModel):
    prices: Optional[Dict[str, str]]
    diff_24h: Optional[Dict[str, str]]
    diff_7d: Optional[Dict[str, str]]
    diff_30d: Optional[Dict[str, str]]
