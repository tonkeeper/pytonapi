from typing import Dict, Any

from pydantic.v1 import BaseModel


class Rates(BaseModel):
    rates: Dict[str, Dict]


class ChartRates(BaseModel):
    points: Dict[str, Any]
