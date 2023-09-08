from typing import Union, List, Dict, Optional

from pydantic.v1 import BaseModel

from pytonapi.schema._address import Address


class AccountStakingInfo(BaseModel):
    pool: str
    amount: int
    pending_deposit: int
    pending_withdraw: int
    ready_withdraw: int


class AccountStaking(BaseModel):
    pools: List[AccountStakingInfo]


class PoolImplementation(BaseModel):
    name: str
    description: str
    url: str
    socials: List[str]


class PoolInfo(BaseModel):
    address: Address
    name: str
    total_amount: int
    implementation: str
    apy: Union[float, int]
    min_stake: int
    cycle_start: int
    cycle_end: int
    verified: bool
    current_nominators: int
    max_nominators: int
    liquid_jetton_master: Optional[str]
    nominators_stake: int
    validator_stake: int


class StakingPoolInfo(BaseModel):
    implementation: PoolImplementation
    pool: PoolInfo


class ApyHistory(BaseModel):
    apy: Union[float, int]
    time: int


class StakingPoolHistory(BaseModel):
    apy: List[ApyHistory]


class StakingPools(BaseModel):
    pools: List[PoolInfo]
    implementations: Dict[str, PoolImplementation]
