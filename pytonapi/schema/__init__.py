from pydantic import BaseModel

from pytonapi.utils import nano_to_amount, raw_to_userfriendly


class Address(BaseModel):
    __root__: str

    def __str__(self) -> str:
        return self.__root__

    def __call__(self) -> str:
        return self.__root__

    def to_raw(self) -> str:
        """
        Converts a TON address in userfriendly format to its raw format.

        :return: The TON address in raw format.
         This should be a string consisting of the workchain ID and key in
         hexadecimal format, separated by a colon.
        """
        return self.__root__

    def to_userfriendly(self, tag=0x11) -> str:
        """
        Converts a raw address string to a user-friendly format.

        :param tag: The tag value to include in the output. Defaults to 0x11.
        :return: The user-friendly address string, encoded in base64 and URL-safe.
        """
        return raw_to_userfriendly(self.__root__, tag=tag)


class Balance(BaseModel):
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
