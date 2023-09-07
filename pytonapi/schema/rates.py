from typing import Dict

from pydantic.v1 import BaseModel


class Rates(BaseModel):
    rates: Dict[str, Dict]
