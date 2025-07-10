from typing import Optional

from pytonapi.base import AsyncTonapiClientBase
from pytonapi.schema.purchases import Purchases


class PurchasesMethod(AsyncTonapiClientBase):

    async def get_purchases_history(
            self,
            account_id: str,
            limit: int = 100,
            before_lt: Optional[int] = None
    ) -> Purchases:
        """
        Get history of purchases.

        :param account_id: account ID
        :param before_lt: omit this parameter to get last invoices
        :param limit: Default value : 100
        :return: :class:`Purchases`
        """
        method = f"v2/purchases/{account_id}/history"
        params = {"limit": limit}
        if before_lt:
            params["before_lt"] = before_lt
        response = await self._get(method=method, params=params)

        return Purchases(**response)
