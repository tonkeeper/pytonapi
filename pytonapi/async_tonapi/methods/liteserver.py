from typing import Dict, Any, Optional, Union

from pytonapi.async_tonapi.client import AsyncTonapiClient
from pytonapi.schema.liteserver import (
    RawMasterChainInfo,
    RawMasterChainInfoExt,
    RawGetBlock,
    RawBlockState,
    RawBlockHeader,
    RawAccountState,
    RawShardInfo,
    RawShardsInfo,
    RawTransactions,
    RawListBlockTransactions,
    RawBlockProof,
    RawConfig,
    RawShardProof,
)


class LiteserverMethod(AsyncTonapiClient):

    async def get_masterchain_info(self) -> RawMasterChainInfo:
        """
        Get raw masterchain info.

        :return: :class:`RawMasterChainInfo`
        """
        method = "v2/liteserver/get_masterchain_info"
        response = await self._get(method=method)

        return RawMasterChainInfo(**response)

    async def get_masterchain_info_ext(self, mode: int) -> RawMasterChainInfoExt:
        """
        Get raw masterchain info ext

        :return: :class:`RawMasterChainInfoExt`
        """
        method = "v2/liteserver/get_masterchain_info_ext"
        params = {"mode": mode}
        response = await self._get(method, params=params)

        return RawMasterChainInfoExt(**response)

    async def get_time(self) -> Union[int, None]:
        """
        Get raw time.

        :return: :class:`int` time
        """
        method = "v2/liteserver/get_time"
        response = await self._get(method=method)

        return response.get("time", None)

    async def get_raw_block(self, block_id: str) -> RawGetBlock:
        """
        Get raw blockchain block.

        :param block_id: block ID:  (workchain,shard,seqno,root_hash,file_hash)
        :return: :class:`RawGetBlock`
        """
        method = f"v2/liteserver/get_block/{block_id}"
        response = await self._get(method=method)

        return RawGetBlock(**response)

    async def get_raw_state(self, block_id: str) -> RawBlockState:
        """
        Get raw blockchain block state.

        :param block_id: block ID:  (workchain,shard,seqno,root_hash,file_hash)
        :return: :class:`RawBlockState`
        """
        method = f"v2/liteserver/get_state/{block_id}"
        response = await self._get(method=method)

        return RawBlockState(**response)

    async def get_raw_header(self, block_id: str) -> RawBlockHeader:
        """
        Get raw blockchain block header.

        :param block_id: block ID:  (workchain,shard,seqno,root_hash,file_hash)
        :return: :class:`RawBlockHeader`
        """
        method = f"v2/liteserver/get_block_header/{block_id}"
        response = await self._get(method=method)

        return RawBlockHeader(**response)

    async def send_message(self, body: Dict[str, Any]) -> Union[int, None]:
        """
        Send raw message to blockchain.

        :param body: Data that is expected
        :return: :class:`int` code
        """
        method = "v2/liteserver/send_message"
        response = await self._post(method=method, body=body)

        return response.get("code", None)

    async def get_account_state(
            self,
            account_address: str,
            target_block: Optional[str] = None,
    ) -> RawAccountState:
        """
        Get raw account state.

        :param account_address: account ID
        :param target_block: target block: (workchain,shard,seqno,root_hash,file_hash)
        :return: :class:`RawAccountState`
        """
        method = f"v2/liteserver/get_account_state/{account_address}"
        params = {"target_block": target_block} if target_block else {}
        response = await self._get(method=method, params=params)

        return RawAccountState(**response)

    async def get_shard_info(
            self,
            block_id: str,
            workchain: int,
            shard: int,
            exact: bool = False,
    ) -> RawShardInfo:
        """
        Get raw shard info.

        :param block_id: block ID:  (workchain,shard,seqno,root_hash,file_hash)
        :param workchain: workchain
        :param shard: shard
        :param exact: exact flag
        :return: :class:`RawShardInfo`
        """
        method = f"v2/liteserver/get_shard_info/{block_id}"
        params = {"workchain": workchain, "shard": shard, "exact": exact}
        response = await self._get(method=method, params=params)

        return RawShardInfo(**response)

    async def get_all_raw_shards_info(self, block_id: str) -> RawShardsInfo:
        """
        Get all raw shards info.

        :param block_id: block ID:  (workchain,shard,seqno,root_hash,file_hash)
        :return: :class:`RawShardsInfo`
        """
        method = f"v2/liteserver/get_all_shards_info/{block_id}"
        response = await self._get(method=method)

        return RawShardsInfo(**response)

    async def get_raw_transactions(
            self,
            account_id: str,
            lt: int,
            hash_: str,
            count: int = 100,
    ) -> RawTransactions:
        """
        Get raw transactions.

        :param account_id: account ID
        :param lt: lt
        :param hash_: hash
        :param count: count
        :return: :class:`RawTransactions`
        """
        method = f"v2/liteserver/get_transactions/{account_id}"
        params = {"lt": lt, "hash": hash_, "count": count}
        response = await self._get(method=method, params=params)

        return RawTransactions(**response)

    async def get_raw_list_block_transaction(
            self,
            block_id: str,
            mode: int,
            count: int = 100,
            account_id: Optional[str] = None,
            lt: Optional[int] = None,
    ) -> RawListBlockTransactions:
        """
        Get raw list block transaction.

        :param block_id: block ID:  (workchain,shard,seqno,root_hash,file_hash)
        :param mode: mode
        :param count: count
        :param account_id: account ID
        :param lt: lt
        :return: :class:`RawListBlockTransactions`
        """
        method = f"v2/liteserver/get_block_transactions/{block_id}"
        params = {
            "mode": mode,
            "count": count,
            "account_id": account_id,
            "lt": lt
        }
        response = await self._get(method=method, params=params)

        return RawListBlockTransactions(**response)

    async def get_block_proof(
            self,
            know_block: str,
            mode: int = 0,
            target_block: Optional[str] = None,
    ) -> RawBlockProof:
        """
        Get raw block proof.

        :param know_block: know block: (workchain,shard,seqno,root_hash,file_hash)
        :param mode: mode 0
        :param target_block: target block: (workchain,shard,seqno,root_hash,file_hash)
        :return: :class:`RawBlockProof`
        """
        method = f"v2/liteserver/get_block_proof/{know_block}"
        params = {
            "know_block": know_block,
            "mode": mode,
        }
        if target_block:
            params["target_block"] = target_block
        response = await self._get(method=method, params=params)

        return RawBlockProof(**response)

    async def get_config_all(
            self,
            block_id: str,
            mode: int = 0,
    ) -> RawConfig:
        """
        Get raw config.

        :param block_id: block ID:  (workchain,shard,seqno,root_hash,file_hash)
        :param mode: mode
        :return: :class:`RawConfig`
        """
        method = f"v2/liteserver/get_config_all/{block_id}"
        params = {"mode": mode}
        response = await self._get(method=method, params=params)

        return RawConfig(**response)

    async def get_shard_block_proof(self, block_id: str) -> RawShardProof:
        """
        Get raw shard block proof.

        :param block_id: block ID:  (workchain,shard,seqno,root_hash,file_hash)
        :return: :class:`RawShardProof`
        """
        method = f"v2/liteserver/get_shard_block_proof/{block_id}"
        response = await self._get(method=method)

        return RawShardProof(**response)
