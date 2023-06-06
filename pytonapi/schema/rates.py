from typing import Dict

from pydantic import BaseModel


class Rates(BaseModel):
    rates: Dict[str, Dict]
