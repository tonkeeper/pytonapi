from pydantic.v1 import BaseModel

from pytonapi.utils import nano_to_amount


class Balance(BaseModel):
    """
    Represents the balance of an account.
    """
    __root__: int

    def __int__(self) -> int:
        return self.__root__

    def __call__(self) -> int:
        return self.__root__

    def to_nano(self) -> int:
        """
        Converts TON value to nanoton.

        :return: The value of the input in nanoton.
        """
        return self.__root__

    def to_amount(self, precision: int = 2) -> float:
        """
        Converts a value from nanoton to TON and rounds it to the specified precision.

        :param precision: The number of decimal places to round the converted value to. Defaults to 2.
        :return: The converted value, in TON, rounded to the specified precision.
        """
        return nano_to_amount(self.__root__, precision=precision)
