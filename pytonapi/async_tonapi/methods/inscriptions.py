from typing import Dict, Optional, Literal

from pytonapi.async_tonapi.client import AsyncTonapiClient
from pytonapi.schema.events import AccountEvents
from pytonapi.schema.inscriptions import InscriptionBalances


class InscriptionsMethod(AsyncTonapiClient):

    async def get_all_inscriptions(
            self,
            account_id: str,
            limit: int = 1000,
            offset: int = 0,
    ) -> InscriptionBalances:
        """
        Get all inscriptions by owner address. It's experimental API and can be dropped in the future.

        :param account_id: account address
        :param limit: Default value : 1000
        :param offset: Default value : 0
        :return: :class:`InscriptionBalances`
        """
        method = f"v2/experimental/accounts/{account_id}/inscriptions"
        params = {"limit": limit, "offset": offset}
        response = await self._get(method=method, params=params)

        return InscriptionBalances(**response)

    async def get_inscription_history(
            self,
            account_id: str,
            before_lt: Optional[int] = None,
            limit: int = 100,
            accept_language: str = "en",
    ) -> AccountEvents:
        """
        Get the transfer inscriptions history for account. It's experimental API and can be dropped in the future.

        :param account_id: account address
        :param before_lt: Default value : 0
        :param limit: Default value : 100
        :param accept_language: Default value : en
        """
        method = f"v2/experimental/accounts/{account_id}/inscriptions/history"
        params = {"limit": limit}
        if before_lt:
            params["before_lt"] = before_lt
        headers = {"Accept-Language": accept_language}
        response = await self._get(method=method, params=params, headers=headers)

        return AccountEvents(**response)

    async def get_inscription_history_by_ticker(
            self,
            account_id: str,
            ticker: str,
            before_lt: Optional[int] = None,
            limit: int = 100,
            accept_language: str = "en",
    ) -> AccountEvents:
        """
        Get the transfer inscriptions history for account. It's experimental API and can be dropped in the future.

        :param account_id: account address
        :param ticker: token ticker
        :param before_lt: Default value : 0
        :param limit: Default value : 100
        :param accept_language: Default value : en
        """
        method = f"v2/experimental/accounts/{account_id}/inscriptions/{ticker}/history"
        params = {"limit": limit}
        if before_lt:
            params["before_lt"] = before_lt
        headers = {"Accept-Language": accept_language}
        response = await self._get(method=method, params=params, headers=headers)

        return AccountEvents(**response)

    async def create_inscription_comment(
            self,
            who: str,
            amount: int,
            type_: Literal["ton20", "gram20"] = "ton20",
            destination: Optional[str] = None,
            comment: Optional[str] = None,
            operation: Literal["transfer"] = "transfer",
            ticker: str = "nano",
    ) -> Dict[str, str]:
        """
        Return comment for making operation with inscription. please don't use it if you don't know what you are doing.

        :param who: account address
        :param amount: amount of tokens
        :param type_: Default value : ton20
        :param destination: Default value : None
        :param comment: Default value : None
        :param operation: Default value : transfer
        :param ticker: Default value : nano
        :return: Dict[str, str]
        """
        method = "v2/experimental/inscriptions/op-template"
        params = {
            "who": who,
            "amount": amount,
            "type": type_,
            "operation": operation,
            "ticker": ticker,
        }
        if destination:
            params["destination"] = destination
        if comment:
            params["comment"] = comment
        response = await self._get(method=method, params=params)

        return response
