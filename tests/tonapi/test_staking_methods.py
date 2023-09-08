from pytonapi import schema
from tests.tonapi import TestTonapi

ACCOUNT_ID = "EQCMVd9ya3yvhyhOWckBUmrHsle3eLqb_em8npZEmbbR-NOe"  # noqa
POOL_ID = "EQCOj4wEjXUR59Kq0KeXUJouY5iAcujkmwJGsYX7qPnITEAM"  # noqa


class TestStakingMethod(TestTonapi):

    def test_get_pool_info(self):
        response = self.tonapi.staking.get_pool_info(POOL_ID)
        self.assertIsInstance(response, schema.staking.StakingPoolInfo)

    def test_get_pool_history(self):
        response = self.tonapi.staking.get_pool_history(POOL_ID)
        self.assertIsInstance(response, schema.staking.StakingPoolHistory)

    def test_get_participating_pools(self):
        response = self.tonapi.staking.get_participating_pools(ACCOUNT_ID)
        self.assertIsInstance(response, schema.staking.AccountStaking)

    def test_get_all_network_pools(self):
        response = self.tonapi.staking.get_all_network_pools(ACCOUNT_ID)
        self.assertIsInstance(response, schema.staking.StakingPools)
