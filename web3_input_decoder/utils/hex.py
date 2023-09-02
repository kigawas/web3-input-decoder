from typing import Union


def hex_to_bytes(data: Union[str, bytes]) -> bytes:
    if isinstance(data, str):
        if data.startswith("0x"):
            data = data[2:]
        data = bytes.fromhex(data)
    return data
