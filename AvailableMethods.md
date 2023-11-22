### Streaming API

- SSE

- [x] v2/sse/accounts/transactions?accounts={accounts}
- [x] v2/sse/accounts/traces?accounts={accounts}
- [x] v2/sse/mempool?accounts={accounts}


- Websocket

- [x] v2/websocket/subscribe_account
- [x] v2/websocket/subscribe_trace
- [x] v2/websocket/subscribe_mempool

### Raw API

- Blockchain

- [x] /v2/blockchain/blocks/{block_id}
- [x] /v2/blockchain/masterchain/{masterchain_seqno}/shards
- [x] /v2/blockchain/blocks/{block_id}/transactions
- [x] /v2/blockchain/blocks/{block_id}/config/raw
- [x] /v2/blockchain/transactions/{transaction_id}
- [x] /v2/blockchain/messages/{msg_id}/transaction
- [x] /v2/blockchain/validators
- [x] /v2/blockchain/masterchain-head
- [x] /v2/blockchain/accounts/{account_id}
- [x] /v2/blockchain/accounts/{account_id}/transactions
- [x] /v2/blockchain/accounts/{account_id}/methods/{method_name}
- [x] /v2/blockchain/message
- [x] /v2/blockchain/config
- [x] /v2/blockchain/config/raw
- [x] /v2/blockchain/accounts/{account_id}/inspect


- Accounts

- [x] /v2/address/{account_id}/parse
- [x] /v2/accounts/_bulk
- [x] /v2/accounts/{account_id}
- [x] /v2/accounts/{account_id}/dns/backresolve
- [x] /v2/accounts/{account_id}/jettons
- [x] /v2/accounts/{account_id}/jettons/history
- [x] /v2/accounts/{account_id}/jettons/{jetton_id}/history
- [x] /v2/accounts/{account_id}/nfts
- [x] /v2/accounts/{account_id}/nfts/history
- [x] /v2/accounts/{account_id}/events
- [x] /v2/accounts/{account_id}/events/{event_id}
- [x] /v2/accounts/{account_id}/traces
- [x] /v2/accounts/{account_id}/subscriptions
- [x] /v2/accounts/{account_id}/reindex
- [x] /v2/accounts/search
- [x] /v2/accounts/{account_id}/dns/expiring
- [x] /v2/accounts/{account_id}/publickey
- [x] /v2/accounts/{account_id}/diff


- Emulation

- [x] /v2/events/emulate
- [x] /v2/traces/emulate
- [x] /v2/wallet/emulate
- [x] /v2/accounts/{account_id}/events/emulate


- NFT

- [x] /v2/accounts/{account_id}/nfts/history
- [x] /v2/nfts/collections
- [x] /v2/nfts/collections/{account_id}
- [x] /v2/nfts/collections/{account_id}/items
- [x] /v2/nfts/_bulk
- [x] /v2/nfts/{account_id}
- [x] /v2/nfts/{account_id}/history


- DNS

- [x] /v2/dns/{domain_name}
- [x] /v2/nfts/{account_id}/history
- [x] /v2/dns/{domain_name}/resolve
- [x] /v2/dns/{domain_name}/bids
- [x] /v2/dns/auctions


- Traces

- [x] /v2/traces/{trace_id}


- Events

- [x] /v2/events/{event_id}


- Jettons

- [x] /v2/jettons
- [x] /v2/jettons/{account_id}
- [x] /v2/jettons/{account_id}/holders
- [x] /v2/events/{event_id}/jettons


- Staking

- [x] /v2/staking/nominator/{account_id}/pools
- [x] /v2/staking/pool/{account_id}
- [x] /v2/staking/pool/{account_id}/history
- [x] /v2/staking/pools


- Storage

- [x] /v2/storage/providers


- Rates

- [x] /v2/rates
- [x] /v2/rates/chart


- Connect

- [x] /v2/tonconnect/payload
- [x] /v2/tonconnect/stateinit


- Wallet

- [x] /v2/wallet/backup
- [x] /v2/wallet/auth/proof
- [x] /v2/pubkeys/{public_key}/wallets
- [x] /v2/wallet/{account_id}/seqno


- Lite Server

- [x] /v2/liteserver/get_masterchain_info
- [x] /v2/liteserver/get_masterchain_info_ext
- [x] /v2/liteserver/get_time
- [x] /v2/liteserver/get_block/{block_id}
- [x] /v2/liteserver/get_state/{block_id}
- [x] /v2/liteserver/get_block_header/{block_id}
- [x] /v2/liteserver/send_message
- [x] /v2/liteserver/get_account_state/{account_id}
- [x] /v2/liteserver/get_shard_info/{block_id}
- [x] /v2/liteserver/get_all_shards_info/{block_id}
- [x] /v2/liteserver/get_transactions/{account_id}
- [x] /v2/liteserver/list_block_transactions/{block_id}
- [x] /v2/liteserver/get_block_proof
- [x] /v2/liteserver/get_config_all/{block_id}
- [x] /v2/liteserver/get_shard_block_proof/{block_id}