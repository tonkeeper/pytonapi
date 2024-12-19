from typing import List

from pytonapi.base import AsyncTonapiClientBase
from pytonapi.schema.webhooks import WebhookCreate, WebhookList, AccountSubscriptions


class WebhooksMethod(AsyncTonapiClientBase):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.base_url = "https://rt.tonapi.io/"

    async def create_webhook(self, endpoint: str) -> WebhookCreate:
        """
        Create a new webhook and return its ID.

        :param endpoint: The webhook endpoint URL to receive transaction events.
        :return: An object containing the ID of the created webhook.
        :rtype: WebhookCreate
        """
        method = "webhooks"
        body = {"endpoint": endpoint}
        response = await self._post(method=method, body=body)
        return WebhookCreate(**response)

    async def list_webhooks(self) -> WebhookList:
        """
        Retrieve a list of all available webhooks.

        :return: A list containing all webhooks with their IDs and endpoints.
        :rtype: WebhookList
        """
        method = "webhooks"
        response = await self._get(method=method)
        return WebhookList(**response)

    async def delete_webhook(self, webhook_id: int) -> None:
        """
        Delete a webhook and all its subscriptions.

        :param webhook_id: The ID of the webhook to delete.
        """
        method = f"webhooks/{webhook_id}"
        await self._delete(method=method)

    async def subscribe_to_account(self, webhook_id: int, accounts: List[str]) -> None:
        """
        Subscribe a webhook to specific account transactions.

        :param webhook_id: The ID of the webhook to subscribe.
        :param accounts: A list of account IDs to subscribe to.
        """
        method = f"webhooks/{webhook_id}/account-tx/subscribe"
        body = {"accounts": [{"account_id": account} for account in accounts]}
        await self._post(method=method, body=body)

    async def unsubscribe_from_account(self, webhook_id: int, accounts: List[str]) -> None:
        """
        Unsubscribe a webhook from specific account transactions.

        :param webhook_id: The ID of the webhook to unsubscribe.
        :param accounts: A list of account IDs to unsubscribe from.
        """
        method = f"webhooks/{webhook_id}/account-tx/unsubscribe"
        body = {"accounts": accounts}
        await self._post(method=method, body=body)

    async def get_subscriptions(self, webhook_id: int, offset: int = 0, limit: int = 10) -> AccountSubscriptions:
        """
        Retrieve the list of subscriptions for a given webhook.

        :param webhook_id: The ID of the webhook.
        :param offset: The offset for pagination. Default is 0.
        :param limit: The maximum number of subscriptions to return. Default is 10.
        :return: A list of account transaction subscriptions with details.
        :rtype: AccountSubscriptions
        """
        method = f"webhooks/{webhook_id}/account-tx/subscriptions"
        params = {"offset": offset, "limit": limit}
        response = await self._get(method=method, params=params)
        return AccountSubscriptions(**response)
