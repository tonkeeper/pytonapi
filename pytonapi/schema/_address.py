from pydantic.v1 import BaseModel

from pytonapi.utils import raw_to_userfriendly


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

    def to_userfriendly(self, bounceable: bool = False) -> str:
        """
        Converts a raw address string to a user-friendly format.

        :param bounceable: The flag indicating if the address is bounceable. Defaults to False.
        :return: The user-friendly address string, encoded in base64 and URL-safe.
        """
        return raw_to_userfriendly(self.__root__, bounceable=bounceable)
