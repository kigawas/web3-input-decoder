from typing import Any, Optional, Union

from .decoder import InputDecoder

__all__ = (
    "decode_constructor",
    "decode_function",
    "InputDecoder",
)


def decode_constructor(
    abi: list[dict],
    tx_input: Union[str, bytes],
    bytecode: Optional[Union[str, bytes]] = None,
) -> list[tuple[str, str, Any]]:
    """Decode constructor transaction input

    Parameters
    ----------
    abi: list[dict]
        Contract ABI
    tx_input: Union[str, bytes]
        Transaction input to decode, with or without deployed contract bytecode
    bytecode: Union[str, bytes], optional
        Optional deployed contract bytecode. If this is set, `tx_input` should include bytecode

    Returns
    -------
    list[tuple[str, str, Any]]
        Decoded type-name-value tuples
    """
    decoder = InputDecoder(abi)  # type:ignore[arg-type]
    return decoder.decode_constructor(tx_input, bytecode).arguments


def decode_function(
    abi: list[dict], tx_input: Union[str, bytes]
) -> list[tuple[str, str, Any]]:
    """Decode function transaction input

    Parameters
    ----------
    abi: list[dict]
        Contract ABI
    tx_input: Union[str, bytes]
        Transaction input to decode

    Returns
    -------
    list[tuple[str, str, Any]]
        Decoded type-name-value tuples
    """
    decoder = InputDecoder(abi)  # type:ignore[arg-type]
    return decoder.decode_function(tx_input).arguments
