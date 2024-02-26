from typing import Optional, Dict, Any

from pytonapi.async_tonapi.client import AsyncTonapiClient
from pytonapi.schema.blockchain import (
    Transactions,
    Transaction,
    Validators,
    BlockchainBlock,
    BlockchainBlocks,
    BlockchainBlockShards,
    BlockchainAccountInspect,
    BlockchainConfig,
    BlockchainRawAccount,
    MethodExecutionResult,
    RawBlockchainConfig,
    ServiceStatus,
)


class BlockchainMethod(AsyncTonapiClient):

    async def status(self) -> ServiceStatus:
        """
        Reduce indexing latency.

        :return: :class:`ServiceStatus`
        """
        method = "v2/status"
        response = await self._get(method=method)

        return ServiceStatus(**response)

    async def get_block_data(self, block_id: str) -> BlockchainBlock:
        """
        Get block data.

        :param block_id: block ID (string), example: "(-1,8000000000000000,4234234)"
        :return: :class:`BlockchainBlock`
        """
        method = f"v2/blockchain/blocks/{block_id}"
        response = await self._get(method=method)

        return BlockchainBlock(**response)

    async def get_block(self, masterchain_seqno: int) -> BlockchainBlockShards:
        """
        Get blockchain block shards.

        :param masterchain_seqno: masterchain block seqno
        :return: :class:`BlockchainBlockShards`
        """
        method = f"v2/blockchain/masterchain/{masterchain_seqno}/shards"
        response = await self._get(method=method)

        return BlockchainBlockShards(**response)

    async def get_blocks(self, masterchain_seqno: int) -> BlockchainBlocks:
        """
        Get all blocks in all shards and workchains between target
        and previous masterchain block according to shards last blocks snapshot in masterchain.
        We don't recommend to build your app around this method because
        it has problem with scalability and will work very slow in the future.

        :param masterchain_seqno: masterchain block seqno
        :return: :class:`BlockchainBlocks`
        """
        method = f"v2/blockchain/masterchain/{masterchain_seqno}/blocks"
        response = await self._get(method=method)

        return BlockchainBlocks(**response)

    async def get_transactions_shards(self, masterchain_seqno: int) -> Transactions:
        """
        Get all transactions in all shards and workchains between target
        and previous masterchain block according to shards last blocks snapshot in masterchain.
        We don't recommend to build your app around this method because
        it has problem with scalability and will work very slow in the future.

        :param masterchain_seqno: masterchain block seqno
        :return: :class:`Transactions`
        """
        method = f"v2/blockchain/masterchain/{masterchain_seqno}/transactions"
        response = await self._get(method=method)

        return Transactions(**response)

    async def get_blockchain_config(self, masterchain_seqno: int) -> BlockchainConfig:
        """
        Get blockchain config from a specific block, if present.

        :param masterchain_seqno: masterchain block seqno
        :return: :class:`BlockchainConfig`
        """
        method = f"v2/blockchain/masterchain/{masterchain_seqno}/config"
        response = await self._get(method=method)

        return BlockchainConfig(**response)

    async def get_raw_blockchain_config(self, masterchain_seqno: int) -> RawBlockchainConfig:
        """
        Get raw blockchain config from a specific block, if present.

        :param masterchain_seqno: masterchain block seqno
        :return: :class:`RawBlockchainConfig`
        """
        method = f"v2/blockchain/masterchain/{masterchain_seqno}/config/raw"
        response = await self._get(method=method)

        return RawBlockchainConfig(**response)

    async def get_transaction_from_block(self, block_id: str) -> Transactions:
        """
        Get transactions from block.

        :param block_id: block ID (string), example: "(-1,8000000000000000,4234234)"
        :return: :class:`Transactions`
        """
        method = f"v2/blockchain/blocks/{block_id}/transactions"
        response = await self._get(method=method)

        return Transactions(**response)

    async def get_transaction_data(self, transaction_id: str) -> Transaction:
        """
        Get transaction data.

        :param transaction_id: Transaction_id ID (string),
         example: "97264395BD65A255A429B11326C84128B7D70FFED7949ABAE3036D506BA38621"
        :return: :class:`Transaction`
        """
        method = f"v2/blockchain/transactions/{transaction_id}"
        response = await self._get(method=method)

        return Transaction(**response)

    async def get_transaction_by_message(self, msg_id: str) -> Transaction:
        """
        Get transaction data by message hash.

        :param msg_id: message ID
        :return: :class:`Transaction`
        """
        method = f"v2/blockchain/messages/{msg_id}/transaction"
        response = await self._get(method=method)

        return Transaction(**response)

    async def get_validators(self) -> Validators:
        """
        Get blockchain validators.

        :return: :class:`Validators`
        """
        method = f"v2/blockchain/validators"
        response = await self._get(method=method)

        return Validators(**response)

    async def get_last_masterchain_block(self) -> BlockchainBlock:
        """
        Get last known masterchain block.

        :return: :class:`BlockchainBlock`
        """
        method = f"v2/blockchain/masterchain-head"
        response = await self._get(method=method)

        return BlockchainBlock(**response)

    async def get_account_info(self, account_id: str) -> BlockchainRawAccount:
        """
        Get low-level information about an account taken directly from the blockchain.

        :param account_id: Account ID
        :return: :class:`BlockchainRawAccount`
        """
        method = f"v2/blockchain/accounts/{account_id}"
        response = await self._get(method=method)

        return BlockchainRawAccount(**response)

    async def get_account_transactions(
            self,
            account_id: str,
            after_lt: Optional[int] = None,
            before_lt: Optional[int] = None,
            limit: int = 100,
    ) -> Transactions:
        """
        Get account transactions.

        :param account_id: account ID
        :param after_lt: omit this parameter to get last transactions
        :param before_lt: omit this parameter to get last transactions
        :param limit: Default value : 100
        :return: :class:`Transactions`
        """
        method = f"v2/blockchain/accounts/{account_id}/transactions"
        params = {"limit": limit}
        if before_lt is not None:
            params["before_lt"] = before_lt
        if after_lt is not None:
            params["after_lt"] = after_lt
        response = await self._get(method=method, params=params)

        return Transactions(**response)

    async def execute_get_method(
            self,
            account_id: str,
            method_name: str,
            *args: Optional[str],
    ) -> MethodExecutionResult:
        """
        Execute get method for account.

        :param account_id: account ID
        :param method_name: contract get method name
        :param args: contract get method args
        :return: :class:`MethodExecutionResult`
        """
        method = f"v2/blockchain/accounts/{account_id}/methods/{method_name}"
        query_params = "&".join(f"args={arg}" for arg in args)
        if query_params:
            method += f"?{query_params}"
        response = await self._get(method=method)

        return MethodExecutionResult(**response)

    async def send_message(self, body: Dict[str, Any]) -> bool:
        """
        Send message to blockchain.

        :param body: both a single boc and a batch of boc serialized in base64 are accepted
        :return: bool
        """
        method = "v2/blockchain/message"
        response = await self._post(method=method, body=body)

        return bool(response)

    async def get_config(self) -> BlockchainConfig:
        """
        Get blockchain config.

        :return: :class:`BlockchainConfig`
        """
        method = "v2/blockchain/config"
        response = await self._get(method=method)

        return BlockchainConfig(**response)

    async def get_raw_config(self) -> RawBlockchainConfig:
        """
        Get raw blockchain config.

        :return: :class:`RawBlockchainConfig`
        """
        method = "v2/blockchain/config/raw"
        response = await self._get(method=method)

        return RawBlockchainConfig(**response)

    async def inspect_account(self, account_id: str) -> BlockchainAccountInspect:
        """
        Blockchain account inspect.

        :param account_id: account ID
        :return: :class:`BlockchainAccountInspect`
        """
        method = f"v2/blockchain/accounts/{account_id}/inspect"
        response = await self._get(method=method)

        return BlockchainAccountInspect(**response)
