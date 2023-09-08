from typing import Optional

from pytonapi.tonapi.client import TonapiClient
from pytonapi.schema.staking import (StakingPoolInfo, AccountStaking,
                                     StakingPoolHistory, StakingPools)


class StakingMethod(TonapiClient):

    def get_participating_pools(self, account_id: str) -> AccountStaking:
        """
        All pools where account participates.

        :param account_id: account ID
        :return: :class:`AccountStaking`
        """
        method = f"v2/staking/nominator/{account_id}/pools"
        response = self._get(method=method)

        return AccountStaking(**response)

    def get_pool_info(self, account_id: str, accept_language: str = "en") -> StakingPoolInfo:
        """
        Stacking pool info.

        :param account_id: account ID
        :param accept_language: Default value : en
        :return: :class:`StakingPoolInfo`
        """
        method = f"v2/staking/pool/{account_id}"
        headers = {"Accept-Language": accept_language}
        response = self._get(method=method, headers=headers)

        return StakingPoolInfo(**response)

    def get_pool_history(self, account_id: str) -> StakingPoolHistory:
        """
        Stacking pool history.

        :param account_id: account ID
        :return: :class:`StakingPoolHistory`
        """
        method = f"v2/staking/pool/{account_id}/history"
        response = self._get(method=method)

        return StakingPoolHistory(**response)

    def get_all_network_pools(self, available_for: str, include_unverified: Optional[bool] = False,
                              accept_language: str = "en") -> StakingPools:
        """
        All pools available in network.

        :param available_for: account ID
        :param include_unverified: return also pools not from
            white list - just compatible by interfaces (maybe dangerous!)
        :param accept_language: Default value : en
        :return: :class:`StakingPools`
        """
        method = f"v2/staking/pools"
        params = {"available_for": available_for,
                  "include_unverified": "true" if include_unverified else "false"}
        headers = {"Accept-Language": accept_language}
        response = self._get(method=method, params=params, headers=headers)

        return StakingPools(**response)
