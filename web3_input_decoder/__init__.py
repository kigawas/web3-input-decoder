from typing import Any, List, Tuple, Union

from eth_abi.abi import decode_abi
from eth_utils import function_abi_to_4byte_selector

from .utils import (
    detect_constructor_arguments,
    get_constructor_type,
    get_types_names,
    hex_to_bytes,
)

__all__ = (
    "decode_constructor",
    "decode_function",
)


def decode_constructor(
    abi: List[dict],
    tx_input: Union[str, bytes],
    bytecode: Union[str, bytes] = None,
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
    type_def = get_constructor_type(abi)["inputs"]
    types, names = get_types_names(type_def)
    tx_input = hex_to_bytes(tx_input)

    if bytecode is not None:
        bytecode_len = len(hex_to_bytes(bytecode))
        tx_input = tx_input[bytecode_len:]
    else:
        tx_input = detect_constructor_arguments(abi, tx_input)

    values = decode_abi(types, tx_input)  # type: ignore
    return [(t, n, v) for t, n, v in zip(types, names, values)]


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
    selector_to_type_def = {}
    for type_def in abi:
        if type_def["type"] == "function":
            selector = function_abi_to_4byte_selector(type_def)
            selector_to_type_def[selector] = type_def

    tx_input = hex_to_bytes(tx_input)
    selector, args = tx_input[:4], tx_input[4:]

    type_def = selector_to_type_def[selector]["inputs"]
    types, names = get_types_names(type_def)

    values = decode_abi(types, args)
    return [(t, n, v) for t, n, v in zip(types, names, values)]
