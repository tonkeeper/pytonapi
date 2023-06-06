import base64
import struct
from typing import Union

import libscrc

__all__ = [
    'raw_to_userfriendly',
    'userfriendly_to_raw',
    'nano_to_amount',
    'amount_to_nano'
]


def raw_to_userfriendly(address: str, tag: int = 0x11) -> str:
    """
    Converts a raw address string to a user-friendly format.

    :param address: address (str): The raw address string in the format "workchain_id:key".
    :param tag: The tag value to include in the output. Defaults to 0x11.
    :return: The user-friendly address string, encoded in base64 and URL-safe.
    """
    workchain_id, key = address.split(':')
    workchain_id = int(workchain_id)
    key = bytearray.fromhex(key)

    short_ints = [j * 256 + i for i, j in zip(*[iter(key)] * 2)]
    payload = struct.pack(f'Bb{"H" * 16}', tag, workchain_id, *short_ints)
    crc = libscrc.xmodem(payload, )
    e_key = payload + struct.pack('>H', crc)

    return base64.urlsafe_b64encode(e_key).decode("utf-8")


def userfriendly_to_raw(address: str) -> str:
    """
    Converts a TON address in userfriendly format to its raw format.

    :param address: The TON address in user-friendly format.
     This should be a string consisting of 48 characters in base64 encoding.
    :return: The TON address in raw format.
     This should be a string consisting of the workchain ID and key in
     hexadecimal format, separated by a colon.
    """
    k = base64.urlsafe_b64decode(address)[1:34]
    workchain_id = struct.unpack('b', k[:1])[0]
    key = k[1:].hex().upper()

    return f'{workchain_id}:{key}'


def nano_to_amount(value: Union[int, float], precision: int = 2) -> float:
    """
    Converts a value from nanoton to TON and rounds it to the specified precision.

    :param value: The value to convert, in nanoton. This should be a positive integer or float.
    :param precision: The number of decimal places to round the converted value to. Defaults to 2.
    :return: The converted value, in TON, rounded to the specified precision.
    """
    converted_value = round(value / 10 ** 9, 9)

    return round(converted_value, precision)


def amount_to_nano(value: Union[int, float]) -> int:
    """
    Converts TON value to nanoton.

    :param value: TON value to be converted. Can be a float or an integer.
    :return: The value of the input in nanoton.
    """
    return int(value * (10 ** 9))
