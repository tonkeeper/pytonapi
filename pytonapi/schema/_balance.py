from pydantic import RootModel

from pytonapi.utils import to_amount, to_nano


class Balance(RootModel[int]):
    """
    Represents the balance of an account.
    """

    def __str__(self) -> str:
        return self.root.__str__()

    def to_nano(self, decimals: int = 9) -> int:
        """
        Converts TON value to nanoton.

        :param decimals: The number of decimal places in the input value. Defaults to 9.
        :return: The value of the input in nanoton.
        """
        return to_nano(self.root, decimals=decimals)

    def to_amount(self, decimals: int = 9, precision: int = 2) -> float:
        """
        Converts a value from nanoton to TON and rounds it to the specified precision.

        :param decimals: The number of decimal places in the converted value. Defaults to 9.
        :param precision: The number of decimal places to round the converted value to. Defaults to 2.
        :return: The converted value, in TON, rounded to the specified precision.
        """
        return to_amount(self.root, decimals=decimals, precision=precision)
