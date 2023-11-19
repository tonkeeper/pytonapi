from typing import List, Optional

from pytonapi.async_tonapi.client import AsyncTonapiClient
from pytonapi.schema.events import AccountEvents
from pytonapi.schema.nft import NftCollections, NftCollection, NftItems, NftItem


class NftMethod(AsyncTonapiClient):

    async def get_collections(self, limit: int = 15, offset: int = 0) -> NftCollections:
        """
        Get NFT collections.

        :param limit: Default value : 15
        :param offset: Default value : 0
        :return: :class:`NftCollections`
        """
        method = "v2/nfts/collections"
        params = {'limit': limit, 'offset': offset}
        response = await self._get(method=method, params=params)

        return NftCollections(**response)

    async def get_collection_by_collection_address(self, account_id: str) -> NftCollection:
        """
        Get NFT collection by collection address.

        :param account_id: Account ID
        :return: :class:`NftCollection`
        """
        method = f"v2/nfts/collections/{account_id}"
        response = await self._get(method=method)

        return NftCollection(**response)

    async def get_items_by_collection_address(
            self,
            account_id: str,
            limit: int = 1000,
            offset: int = 0,
    ) -> NftItems:
        """
        Get NFT items from collection by collection address.

        :param account_id: Account ID
        :param limit: Default value: 1000
        :param offset: Default value: 0
        :return: :class:`NftItems`
        """
        method = f"v2/nfts/collections/{account_id}/items"
        params = {'limit': limit, 'offset': offset}
        response = await self._get(method=method, params=params)

        return NftItems(**response)

    async def get_all_items_by_collection_address(self, account_id: str) -> NftItems:
        """
        Get all NFT items from collection by collection address.

        :param account_id: Account ID
        :return: :class:`NftItems`
        """
        nft_items: List[NftItem] = []
        offset, limit = 0, 1000

        while True:
            result = await self.get_items_by_collection_address(
                account_id=account_id, limit=limit, offset=offset,
            )
            nft_items += result.nft_items
            offset += limit

            if len(result.nft_items) != limit:
                break

        return NftItems(nft_items=nft_items)

    async def get_item_by_address(self, account_id: str) -> NftItem:
        """
        Get NFT item by its address.

        :param account_id: Account ID
        :return: :class:`NftItem`
        """
        method = f"v2/nfts/{account_id}"
        response = await self._get(method=method)

        return NftItem(**response)

    async def get_bulk_items(self, account_ids: List[str]) -> NftItems:
        """
        Get NFT items by their addresses.

        :param account_ids: A list of account IDs
        :return: :class:`NftItems`
        """
        method = f"v2/nfts/_bulk"
        params = {"account_ids": account_ids}
        response = await self._post(method=method, body=params)

        return NftItems(**response)

    async def get_nft_history(
            self,
            account_id: str,
            limit: int = 100,
            before_lt: Optional[int] = None,
            accept_language: str = "en",
            subject_only: bool = False,
            start_date: Optional[int] = None,
            end_date: Optional[int] = None,
    ) -> AccountEvents:
        """
        Get the transfer NFTs history for account.

        :param account_id: Account ID
        :param limit: Default value: 100
        :param before_lt: Default value: None (omit this parameter to get last events)
        :param accept_language: Default value: en
        :param subject_only: Default value: False
        :param start_date: Default value: None
        :param end_date: Default value: None
        :return: :class:`AccountEvents`
        """
        method = f"v2/nfts/{account_id}/history"
        params = {"limit": limit}
        if before_lt:
            params["before_lt"] = before_lt
        if subject_only:
            params["subject_only"] = "true"
        if start_date:
            params["start_date"] = start_date
        if end_date:
            params["end_date"] = end_date
        headers = {"Accept-Language": accept_language}
        response = await self._get(method=method, params=params, headers=headers)

        return AccountEvents(**response)
