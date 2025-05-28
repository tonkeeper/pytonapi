from typing import Any, Dict, List, Optional

from pytonapi.base import AsyncTonapiClientBase
from pytonapi.schema.accounts import (
    Account,
    Accounts,
    FoundAccounts,
    Subscriptions,
    DnsExpiring,
    PublicKey,
    BalanceChange,
)
from pytonapi.schema.domains import DomainNames
from pytonapi.schema.events import AccountEvents, AccountEvent
from pytonapi.schema.jettons import JettonBalance, JettonsBalances, JettonOperations
from pytonapi.schema.multisig import Multisigs
from pytonapi.schema.nft import NftItems, NftOperations
from pytonapi.schema.traces import TraceIds


class AccountsMethod(AsyncTonapiClientBase):

    async def get_bulk_info(self, account_ids: List[str]) -> Accounts:
        """
        Get human-friendly information about multiple accounts without low-level details.

        :param account_ids: List of account IDs
        :return: :class:`Accounts`
        """
        method = f"v2/accounts/_bulk"
        params = {"account_ids": account_ids}
        response = await self._post(method=method, body=params)

        return Accounts(**response)

    async def get_info(self, account_id: str) -> Account:
        """
        Get human-friendly information about an account without low-level details.

        :param account_id: Account ID
        :return: :class:`Account`
        """
        method = f"v2/accounts/{account_id}"
        response = await self._get(method=method)

        return Account(**response)

    async def get_domains(self, account_id: str) -> DomainNames:
        """
        Get domains for wallet account.

        :param account_id: account ID
        :return: :class:`DomainNames`
        """
        method = f"v2/accounts/{account_id}/dns/backresolve"
        response = await self._get(method=method)

        return DomainNames(**response)

    async def get_jettons_balances(
            self,
            account_id: str,
            currencies: Optional[List[str]] = None,
            supported_extensions: Optional[List[str]] = None,
    ) -> JettonsBalances:
        """
        Get all Jettons balances by owner address.

        :param account_id: account ID
        :param currencies: accept ton and all possible fiat currencies, separated by commas
        :param supported_extensions: comma separated list supported extensions
        :return: :class:`JettonsBalances`
        """
        method = f"v2/accounts/{account_id}/jettons"
        params = {"supported_extensions": ",".join(supported_extensions)} if supported_extensions else {}
        if currencies:
            params["currencies"] = ",".join(currencies)
        response = await self._get(method=method, params=params)

        return JettonsBalances(**response)

    async def get_jetton_balance(
            self,
            account_id: str,
            jetton_id: str,
            currencies: Optional[List[str]] = None,
            supported_extensions: Optional[List[str]] = None,
    ) -> JettonBalance:
        """
        Get Jetton balance by owner address

        :param account_id: account ID
        :param jetton_id: jetton ID
        :param currencies: accept ton and all possible fiat currencies, separated by commas
        :param supported_extensions: comma separated list supported extensions
        :return: :class:`JettonBalance`
        """
        method = f"v2/accounts/{account_id}/jettons/{jetton_id}"
        params = {"supported_extensions": ",".join(supported_extensions)} if supported_extensions else {}
        if currencies:
            params["currencies"] = ",".join(currencies)
        response = await self._get(method=method, params=params)

        return JettonBalance(**response)

    async def get_jettons_history(
            self,
            account_id: str,
            limit: int = 100,
            before_lt: Optional[int] = None,
    ) -> JettonOperations:
        """
        Get the transfer jettons history for account.

        :param account_id: account ID
        :param limit: Default value: 100
        :param before_lt: omit this parameter to get last events
        :return: :class:`JettonOperations`
        """
        method = f"v2/accounts/{account_id}/jettons/history"
        params = {"limit": limit}
        if before_lt is not None:
            params["before_lt"] = before_lt
        response = await self._get(method=method, params=params)

        return JettonOperations(**response)

    async def get_nfts(
            self,
            account_id: str,
            limit: int = 1000,
            offset: int = 0,
            collection: Optional[str] = None,
            indirect_ownership: bool = False,
    ) -> NftItems:
        """
        Get NFT items by owner address.

        :param account_id: account ID
        :param limit: Default value: 1000
        :param collection: filter NFT by collection address
        :param offset: Default value: 0
        :param indirect_ownership: Selling nft items in ton implemented usually via transfer items
         to special selling account. This option enables including items which owned not directly.
        :return: :class:`NftItems`
        """
        method = f"v2/accounts/{account_id}/nfts"
        params = {
            "limit": limit,
            "offset": offset,
            "indirect_ownership": "true" if indirect_ownership else "false"
        }
        if collection:
            params["collection"] = collection
        response = await self._get(method=method, params=params)

        return NftItems(**response)

    async def get_events(
            self,
            account_id: str,
            limit: int = 100,
            before_lt: Optional[int] = None,
            accept_language: str = "en",
            initiator: bool = False,
            subject_only: bool = False,
            start_date: Optional[int] = None,
            end_date: Optional[int] = None,
    ) -> AccountEvents:
        """
        Get events for an account. Each event is built on top of a trace which is a series of transactions
        caused by one inbound message. TonAPI looks for known patterns inside the trace and splits the trace
        into actions, where a single action represents a meaningful high-level operation like a Jetton
        Transfer or an NFT Purchase. Actions are expected to be shown to users. It is advised not to build
        any logic on top of actions because actions can be changed at any time.

        :param account_id: account ID
        :param limit: Default value: 100
        :param before_lt: omit this parameter to get last events
        :param initiator: Show only events that are initiated by this account. Default value : false
        :param accept_language: Default value: en
        :param subject_only: filter actions where requested account is not real subject
          (for example sender or receiver jettons). Default value: False
        :param start_date: Default value: None
        :param end_date: Default value: None
        :return: :class:`AccountEvents`
        """
        method = f"v2/accounts/{account_id}/events"
        params = {
            "limit": limit,
            "initiator": initiator,
            "subject_only": subject_only
        }
        if before_lt:
            params["before_lt"] = before_lt
        if start_date:
            params["start_date"] = start_date
        if end_date:
            params["end_date"] = end_date
        headers = {"Accept-Language": accept_language}
        response = await self._get(method=method, params=params, headers=headers)

        return AccountEvents(**response)

    async def get_event(
            self,
            account_id: str,
            event_id: str,
            accept_language: str = "en",
            subject_only: Optional[bool] = False,
    ) -> AccountEvent:
        """
        Get event for an account by event_id

        :param account_id: account ID
        :param event_id: event ID
        :param accept_language: Default value: en
        :param subject_only: Default value: False
        :return: :class:`AccountEvent`
        """
        method = f"v2/accounts/{account_id}/events/{event_id}"
        params = {"subject_only": subject_only} if subject_only else {}
        headers = {"Accept-Language": accept_language}
        response = await self._get(method=method, params=params, headers=headers)

        return AccountEvent(**response)

    async def get_traces(self, account_id: str, limit: int = 100, before_lt: Optional[int] = None) -> TraceIds:
        """
        Get traces for account.

        :param account_id: account ID
        :param limit: Default value: 100
        :param before_lt: omit this parameter to get last events
        :return: :class:`TraceIds`
        """
        method = f"v2/accounts/{account_id}/traces"
        params = {"limit": limit}
        if before_lt is not None:
            params["before_lt"] = before_lt
        response = await self._get(method=method, params=params)

        return TraceIds(**response)

    async def get_nft_history(
            self,
            account_id: str,
            limit: int = 100,
            before_lt: Optional[int] = None,
            accept_language: str = "en",
    ) -> NftOperations:
        """
        Get the transfer nft history.

        :param account_id: account ID
        :param limit: Default value: 100
        :param before_lt: omit this parameter to get last events
        :param accept_language: Default value: en
        :return: :class:`NftOperations`
        """
        method = f"v2/accounts/{account_id}/nfts/history"
        params = {"limit": limit}
        if before_lt is not None:
            params["before_lt"] = before_lt
        headers = {"Accept-Language": accept_language}
        response = await self._get(method=method, params=params, headers=headers)

        return NftOperations(**response)

    async def get_subscriptions(self, account_id: str) -> Subscriptions:
        """
        Get all subscriptions by wallet address

        :param account_id: account ID
        :return: :class:`Subscriptions`
        """
        method = f"v2/accounts/{account_id}/subscriptions"
        response = await self._get(method=method)

        return Subscriptions(**response)

    async def reindex(self, account_id: str) -> None:
        """
        Update internal cache for a particular account

        :param account_id: account ID
        :return: :class:`bool`
        """
        method = f"v2/accounts/{account_id}/reindex"
        await self._post(method=method)

    async def search_by_domain(self, name: str) -> FoundAccounts:
        """
        Search by account domain name.

        :param name: domain name
        :return: :class:`FoundAccounts`
        """
        method = f"v2/accounts/search"
        params = {"name": name}
        response = await self._get(method=method, params=params)

        return FoundAccounts(**response)

    async def get_expiring_dns(self, account_id: str, period: Optional[int] = None) -> DnsExpiring:
        """
        Get expiring account .ton dns.

        :param account_id: account ID
        :param period: number of days before expiration
        :return: :class:`DnsExpiring`
        """
        method = f"v2/accounts/{account_id}/dns/expiring"
        params = {"period": period} if period else {}
        response = await self._get(method=method, params=params)

        return DnsExpiring(**response)

    async def get_public_key(self, account_id: str) -> PublicKey:
        """
        Get public key by account id.

        :param account_id: account ID
        :return: :class:`PublicKey`
        """
        method = f"v2/accounts/{account_id}/publickey"
        response = await self._get(method=method)

        return PublicKey(**response)

    async def get_account_multisigs(self, account_id: str) -> Multisigs:
        """
        Get account's multisigs.

        :param account_id: account ID
        :return: :class:`PublicKey`
        """
        method = f"v2/accounts/{account_id}/multisigs"
        response = await self._get(method=method)

        return Multisigs(**response)

    async def get_balance_change(
            self,
            account_id: str,
            start_date: int,
            end_date: int,
    ) -> BalanceChange:
        """
        Get account's balance change.

        :param account_id: account ID
        :param start_date: start date
        :param end_date: end date
        :return: :class:`BalanceChange`
        """
        method = f"v2/accounts/{account_id}/diff"
        params = {"start_date": start_date, "end_date": end_date}
        response = await self._get(method=method, params=params)

        return BalanceChange(**response)

    async def get_extra_currency_history(
            self,
            account_id: str,
            currency_id: int,
            limit: int = 100,
            accept_language: str = "en",
            before_lt: Optional[int] = None,
            start_date: Optional[int] = None,
            end_date: Optional[int] = None,
    ) -> AccountEvents:
        """
        Get extra currency history.

        :param account_id: account ID
        :param currency_id: currency ID
        :param limit: Default value: 100
        :param before_lt: omit this parameter to get last events
        :param accept_language: Default value: en
        :param start_date: start date
        :param end_date: end date
        :return: :class:`AccountEvents`
        """
        method = f"/v2/accounts/{account_id}/extra-currency/{currency_id}/history"
        params = {"limit": limit}
        if before_lt is not None:
            params["before_lt"] = before_lt
        if start_date is not None:
            params["start_date"] = start_date
        if end_date is not None:
            params["end_date"] = end_date
        headers = {"Accept-Language": accept_language}
        response = await self._get(method=method, params=params, headers=headers)

        return AccountEvents(**response)

    async def get_jettons_history_by_jetton(
            self,
            account_id: str,
            jetton_id: int,
            limit: int = 100,
            accept_language: str = "en",
            before_lt: Optional[int] = None,
            start_date: Optional[int] = None,
            end_date: Optional[int] = None,
    ) -> JettonOperations:
        """
        Get jettons history by jetton master address.

        :param account_id: account ID
        :param jetton_id: jetton ID
        :param limit: Default value: 100
        :param before_lt: omit this parameter to get last events
        :param accept_language: Default value: en
        :param start_date: start date
        :param end_date: end date
        :return: :class:`JettonOperations`
        """
        method = f"/v2/jettons/{jetton_id}/accounts/{account_id}/history"
        params = {"limit": limit}
        if before_lt is not None:
            params["before_lt"] = before_lt
        if start_date is not None:
            params["start_date"] = start_date
        if end_date is not None:
            params["end_date"] = end_date
        headers = {"Accept-Language": accept_language}
        response = await self._get(method=method, params=params, headers=headers)

        return JettonOperations(**response)

    async def emulate_event(
            self,
            account_id: str,
            body: Dict[str, Any],
            accept_language: str = "en",
            ignore_signature_check: Optional[bool] = None,
    ) -> AccountEvent:
        """
        Emulate sending message to blockchain.

        :param account_id: account ID
        :param body: Request body with `boc`: both a single boc and a batch of boc serialized in base64 are accepted.
                    {
                        "boc": "base64 string"
                    }
        :param accept_language: Default value: en
        :param ignore_signature_check: Default value: None
        """
        method = f"v2/accounts/{account_id}/events/emulate"
        params = {"ignore_signature_check": ignore_signature_check} if ignore_signature_check is not None else {}
        headers = {"Accept-Language": accept_language}
        response = await self._post(method=method, params=params, body=body, headers=headers)

        return AccountEvent(**response)
