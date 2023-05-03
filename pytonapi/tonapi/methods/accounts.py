from pytonapi.tonapi.client import TonapiClient

from pytonapi.schema.accounts import Account
from pytonapi.schema.domains import DomainNames
from pytonapi.schema.jettons import JettonsBalances
from pytonapi.schema.nft import NftItems
from pytonapi.schema.traces import TraceIds


class AccountMethod(TonapiClient):

    def get_info(self, account_id: str) -> Account:
        """
        Get human-friendly information about an account without low-level details.

        :param account_id: Account ID
        :return: :class:`Account`
        """
        method = f"v2/accounts/{account_id}"
        response = self._request(method=method)

        return Account(**response)

    def get_domains(self, account_id: str) -> DomainNames:
        """
        Get domains for wallet account.

        :param account_id: account ID
        :return: :class:`DomainNames`
        """
        method = f"v2/accounts/{account_id}/dns/backresolve"
        response = self._request(method=method)

        return DomainNames(**response)

    def get_jettons_balances(self, account_id: str) -> JettonsBalances:
        """
        Get all Jettons balances by owner address.

        :param account_id: account ID
        :return: :class:`JettonsBalances`
        """
        method = f"v2/accounts/{account_id}/jettons"
        response = self._request(method=method)

        return JettonsBalances(**response)

    def get_nfts(self, account_id: str, limit: int = 1000, offset: int = 0,
                 indirect_ownership: bool = False) -> NftItems:
        """
        Get NFT items by owner address.

        :param account_id: account ID
        :param limit: Default value : 1000
        :param offset: Default value : 0
        :param indirect_ownership: Selling nft items in ton implemented usually via transfer items
         to special selling account. This option enables including items which owned not directly.
        :return: :class:`NftItems`
        """
        method = f"v2/accounts/{account_id}/nfts"
        params = {
            "limit": limit, "offset": offset,
            'indirect_ownership': 'true' if indirect_ownership else 'false'
        }
        response = self._request(method=method, params=params)

        return NftItems(**response)

    def get_all_nfts(self, account_id: str) -> NftItems:
        """
        Get all NFT items by owner address.

        :param account_id: account ID
        :return: :class:`NftItems`
        """
        nft_items = []
        offset, limit = 0, 1000

        while True:
            result = self.get_nfts(
                account_id=account_id, limit=limit, offset=offset,
                indirect_ownership=True,
            )
            nft_items += result.nft_items
            offset += limit

            if len(result.nft_items) != limit:
                break

        return NftItems(nft_items=nft_items)

    def get_traces(self, account_id: str, limit: int = 100) -> TraceIds:
        """
        Get traces for account.

        :param account_id: account ID
        :param limit: Default value : 100
        :return: :class:`TraceIds`
        """
        method = f"v2/accounts/{account_id}/traces"
        params = {"limit": limit}
        response = self._request(method=method, params=params)

        return TraceIds(**response)
