from pytonapi.tonapi.client import TonapiClient

from pytonapi.schema.dns import DNSRecord
from pytonapi.schema.domains import DomainBids


class DnsMethod(TonapiClient):

    def resolve(self, domain_name: str) -> DNSRecord:
        """
        DNS resolve for domain name.

        :param domain_name: domain name with .ton or .t.me
        :return: :class:`DNSRecord`
        """
        method = f"v2/dns/{domain_name}/resolve"
        response = self._get(method=method)

        return DNSRecord(**response)

    def bids(self, domain_name: str) -> DomainBids:
        """
        Get domain bids.

        :param domain_name: domain name with .ton or .t.me
        :return: :class:`DomainBids`
        """
        method = f"v2/dns/{domain_name}/bids"
        response = self._get(method=method)

        return DomainBids(**response)
