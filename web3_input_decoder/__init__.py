from typing import Any, List, Optional, Tuple, Union

from .decoder import InputDecoder

__all__ = (
    "decode_constructor",
    "decode_function",
    "InputDecoder",
)


def decode_constructor(
    abi: List[dict],
    tx_input: Union[str, bytes],
    bytecode: Optional[Union[str, bytes]] = None,
) -> List[Tuple[str, str, Any]]:
    """Decode constructor transaction input

    Parameters
    ----------
    abi: List[dict]
        Contract ABI
    tx_input: Union[str, bytes]
        Transaction input to decode, with or without deployed contract bytecode
    bytecode: Union[str, bytes], optional
        Optional deployed contract bytecode. If this is set, `tx_input` should include bytecode

    Returns
    -------
    List[Tuple[str, str, Any]]
        Decoded type-name-value tuples
    """
    decoder = InputDecoder(abi)
    return decoder.decode_constructor(tx_input, bytecode).arguments


def decode_function(
    abi: List[dict], tx_input: Union[str, bytes]
) -> List[Tuple[str, str, Any]]:
    """Decode function transaction input

    Parameters
    ----------
    abi: List[dict]
        Contract ABI
    tx_input: Union[str, bytes]
        Transaction input to decode

    Returns
    -------
    List[Tuple[str, str, Any]]
        Decoded type-name-value tuples
    """
    decoder = InputDecoder(abi)
    return decoder.decode_function(tx_input).arguments
