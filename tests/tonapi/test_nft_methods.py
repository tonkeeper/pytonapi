from pytonapi import schema
from tests.tonapi import TestTonapi

ACCOUNT_ID_COLLECTION = "EQAG2BH0JlmFkbMrLEnyn2bIITaOSssd4WdisE4BdFMkZbir"  # noqa
ACCOUNT_ID_NFT = "EQBSZKEvqoiuPUCFz-CHtpVxAwg1F8PyjZhWAJL2yeujn0_H"  # noqa


class TestNftMethod(TestTonapi):

    def test_get_collections(self):
        response = self.tonapi.nft.get_collections()
        self.assertIsInstance(response, schema.nft.NftCollections)

    def test_get_collection_by_collection_address(self):
        response = self.tonapi.nft.get_collection_by_collection_address(ACCOUNT_ID_COLLECTION)
        self.assertIsInstance(response, schema.nft.NftCollection)

    def test_get_items_by_collection_address(self):
        response = self.tonapi.nft.get_items_by_collection_address(ACCOUNT_ID_COLLECTION)
        self.assertIsInstance(response, schema.nft.NftItems)

    def test_get_all_items_by_collection_address(self):
        response = self.tonapi.nft.get_all_items_by_collection_address(ACCOUNT_ID_COLLECTION)
        self.assertIsInstance(response, schema.nft.NftItems)

    def test_get_item_by_address(self):
        response = self.tonapi.nft.get_item_by_address(ACCOUNT_ID_NFT)
        self.assertIsInstance(response, schema.nft.NftItem)
