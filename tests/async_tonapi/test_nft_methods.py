from pytonapi import schema
from tests.async_tonapi import TestAsyncTonapi

ACCOUNT_ID_COLLECTION = "EQAG2BH0JlmFkbMrLEnyn2bIITaOSssd4WdisE4BdFMkZbir"  # noqa
ACCOUNT_ID_NFT = "EQBSZKEvqoiuPUCFz-CHtpVxAwg1F8PyjZhWAJL2yeujn0_H"  # noqa


class TestNftMethod(TestAsyncTonapi):

    async def test_get_collections(self):
        response = await self.tonapi.nft.get_collections()
        self.assertIsInstance(response, schema.nft.NftCollections)

    async def test_get_collection_by_collection_address(self):
        response = await self.tonapi.nft.get_collection_by_collection_address(ACCOUNT_ID_COLLECTION)
        self.assertIsInstance(response, schema.nft.NftCollection)

    async def test_get_items_by_collection_address(self):
        response = await self.tonapi.nft.get_items_by_collection_address(ACCOUNT_ID_COLLECTION)
        self.assertIsInstance(response, schema.nft.NftItems)

    async def test_get_all_items_by_collection_address(self):
        response = await self.tonapi.nft.get_all_items_by_collection_address(ACCOUNT_ID_COLLECTION)
        self.assertIsInstance(response, schema.nft.NftItems)

    async def test_get_item_by_address(self):
        response = await self.tonapi.nft.get_item_by_address(ACCOUNT_ID_NFT)
        self.assertIsInstance(response, schema.nft.NftItem)
