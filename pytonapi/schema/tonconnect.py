from pydantic.v1 import BaseModel


class TonconnectPayload(BaseModel):
    payload: str


class AccountInfoByStateInit(BaseModel):
    public_key: str
    address: str
