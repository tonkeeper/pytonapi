from pydantic import RootModel

from pytonapi.utils import raw_to_userfriendly


class Address(RootModel[str]):
    """
    Represents a TON address.
    """

    def __str__(self) -> str:
        return self.root

    def to_raw(self) -> str:
        """
        Converts a TON address in userfriendly format to its raw format.

        :return: The TON address in raw format.
        """
        return self.root

    def to_userfriendly(self, is_bounceable: bool = False) -> str:
        """
        Converts a raw address string to a user-friendly format.

        :param is_bounceable: The flag indicating if the address is bounceable. Defaults to False.
        :return: The user-friendly address string.
        """
        return raw_to_userfriendly(self.root, is_bounceable)
