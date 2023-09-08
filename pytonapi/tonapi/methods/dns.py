from pytonapi.tonapi.client import TonapiClient

from pytonapi.schema.dns import DNSRecord, Auctions
from pytonapi.schema.domains import DomainBids, DomainInfo


class DnsMethod(TonapiClient):

    def get_info(self, domain_name: str) -> DomainInfo:
        """
        Get full information about domain name.

        :param domain_name: domain name with .ton or .t.me
        :return: :class:`DomainInfo`
        """
        method = f"v2/dns/{domain_name}"
        response = self._get(method=method)

        return DomainInfo(**response)

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

    def get_auctions(self, tld: str = "ton") -> Auctions:
        """
        Get all auctions.

        :param tld: domain filter for current auctions "ton" or "t.me"
        :return: :class:`Auctions`
        """
        method = f"v2/dns/auctions"
        params = {"tld": tld}
        response = self._get(method=method, params=params)

        return Auctions(**response)
