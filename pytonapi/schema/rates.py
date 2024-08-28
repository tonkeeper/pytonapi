from typing import Dict, Optional, List, Union

from pydantic import BaseModel


class Rates(BaseModel):
    rates: Dict[str, Dict]


class ChartRates(BaseModel):
    points: List[List[Union[str, float]]]


class TokenRates(BaseModel):
    prices: Optional[Dict[str, str]] = None
    diff_24h: Optional[Dict[str, str]] = None
    diff_7d: Optional[Dict[str, str]] = None
    diff_30d: Optional[Dict[str, str]] = None
