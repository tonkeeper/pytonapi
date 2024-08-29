from pydantic import BaseModel


class AddressFormB64(BaseModel):
    b64: str
    b64url: str


class AddressForm(BaseModel):
    raw_form: str
    bounceable: AddressFormB64
    non_bounceable: AddressFormB64
    given_type: str
    test_only: bool


class ServiceStatus(BaseModel):
    rest_online: bool
    indexing_latency: int
    last_known_masterchain_seqno: int
