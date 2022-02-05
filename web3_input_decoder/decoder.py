from dataclasses import dataclass
from typing import Any, List, Tuple, Union

from eth_abi.abi import decode_abi
from eth_utils.abi import function_abi_to_4byte_selector

from .exceptions import InputDataError
from .utils import (
    detect_constructor_arguments,
    get_constructor_type,
    get_types_names,
    hex_to_bytes,
)


@dataclass(frozen=True)
class ContractCall:
    name: str
    arguments: List[Tuple[str, str, Any]]


class InputDecoder:
    def __init__(self, abi: List[dict]):
        self._constructor_type_def = get_constructor_type(abi)
        self._selector_to_type_def = {}
        for type_def in abi:
            if type_def["type"] == "function":
                selector = function_abi_to_4byte_selector(type_def)
                self._selector_to_type_def[selector] = type_def

    def decode_function(self, tx_input: Union[str, bytes]):
        tx_input = hex_to_bytes(tx_input)
        selector, args = tx_input[:4], tx_input[4:]
        if selector not in self._selector_to_type_def:
            raise InputDataError("Specified method not found in ABI")

        type_def = self._selector_to_type_def[selector]

        types, names = get_types_names(type_def["inputs"])
        values = decode_abi(types, args)

        return ContractCall(
            type_def["name"],
            [(t, n, v) for t, n, v in zip(types, names, values)],
        )

    def decode_constructor(
        self,
        tx_input: Union[str, bytes],
        bytecode: Union[str, bytes] = None,
    ):
        tx_input = hex_to_bytes(tx_input)

        if bytecode is not None:
            bytecode_len = len(hex_to_bytes(bytecode))
            tx_input = tx_input[bytecode_len:]
        else:
            tx_input = detect_constructor_arguments(
                self._constructor_type_def, tx_input
            )

        types, names = get_types_names(self._constructor_type_def["inputs"])
        values = decode_abi(types, tx_input)

        return ContractCall(
            "constructor",
            [(t, n, v) for t, n, v in zip(types, names, values)],
        )
