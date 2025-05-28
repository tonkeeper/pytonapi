from pydantic import BaseModel


class EcPreview(BaseModel):
    id: int
    symbol: str
    decimals: int
    image: str
