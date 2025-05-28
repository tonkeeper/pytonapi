from pytonapi.base import AsyncTonapiClientBase
from pytonapi.schema.extra_currency import EcPreview


class ExtraCurrencyMethod(AsyncTonapiClientBase):

    async def get_info(self, currency_id: int) -> EcPreview:
        """
        Get extra currency preview.

        :param currency_id: currency ID
        :return: :class:`EcPreview`
        """
        method = f"v2/extra-currency/{currency_id}"
        response = await self._get(method=method)

        return EcPreview(**response)
