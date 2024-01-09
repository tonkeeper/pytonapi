import base64
import struct
from typing import Union

__all__ = [
    'raw_to_userfriendly',
    'userfriendly_to_raw',
    'nano_to_amount',
    'amount_to_nano'
]


def _calculate_crc_xmodem(payload: bytes) -> int:
    crc = 0
    poly = 0x1021  # CRC-16 Xmodem polynomial

    for byte in payload:
        crc ^= (byte << 8)  # XOR with the next byte

        for _ in range(8):
            if crc & 0x8000:
                crc = (crc << 1) ^ poly
            else:
                crc <<= 1

    return crc & 0xFFFF  # Keep only the lower 16 bits


def raw_to_userfriendly(address: str, is_bounceable: bool = False) -> str:
    """
    Converts a raw address string to a user-friendly format.

    :param address: The raw address string in the format "workchain_id:key".
    :param is_bounceable: The flag indicating if the address is bounceable. Defaults to False.
    :return: The user-friendly address string, encoded in base64 and URL-safe.
    """
    tag = 0x11 if is_bounceable else 0x51
    workchain_id, key = address.split(':')
    workchain_id = int(workchain_id)
    key = bytearray.fromhex(key)

    short_ints = [j * 256 + i for i, j in zip(*[iter(key)] * 2)]
    payload = struct.pack(f'Bb{"H" * 16}', tag, workchain_id, *short_ints)
    crc = _calculate_crc_xmodem(payload)
    encoded_key = payload + struct.pack('>H', crc)

    return base64.urlsafe_b64encode(encoded_key).decode("utf-8")


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
    key = k[1:].hex().lower()

    return f'{workchain_id}:{key}'


def nano_to_amount(value: int, precision: int = 2) -> Union[float, int]:
    """
    Converts a value from nanoton to TON and rounds it to the specified precision.

    :param value: The value to convert, in nanoton. This should be a positive integer.
    :param precision: The number of decimal places to round the converted value to. Defaults to 2.
    :return: The converted value in TON, rounded to the specified precision.
    """
    if not isinstance(value, int) or value < 0:
        raise ValueError("Value must be a positive integer.")

    if not isinstance(precision, int) or precision < 0:
        raise ValueError("Precision must be a non-negative integer.")

    ton_value = value / 1e9
    rounded_ton_value = round(ton_value, precision)

    return rounded_ton_value if rounded_ton_value % 1 != 0 else int(rounded_ton_value)


def amount_to_nano(value: Union[int, float]) -> int:
    """
    Converts TON value to nanoton.

    :param value: TON value to be converted. Can be a float or an integer.
    :return: The value of the input in nanoton.
    """
    if not isinstance(value, (int, float)):
        raise ValueError("Value must be a positive integer or float.")

    return int(value * 1e9)
