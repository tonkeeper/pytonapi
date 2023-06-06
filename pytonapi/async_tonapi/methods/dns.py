from pytonapi.async_tonapi.client import AsyncTonapiClient
from pytonapi.schema.dns import DNSRecord
from pytonapi.schema.domains import DomainBids


class DnsMethod(AsyncTonapiClient):

    async def resolve(self, domain_name: str) -> DNSRecord:
        """
        DNS resolve for domain name.

        :param domain_name: domain name with .ton or .t.me
        :return: :class:`DNSRecord`
        """
        method = f"v2/dns/{domain_name}/resolve"
        response = await self._get(method=method)

        return DNSRecord(**response)

    async def bids(self, domain_name: str) -> DomainBids:
        """
        Get domain bids.

        :param domain_name: domain name with .ton or .t.me
        :return: :class:`DomainBids`
        """
        method = f"v2/dns/{domain_name}/bids"
        response = await self._get(method=method)

        return DomainBids(**response)
