from dataclasses import dataclass
from typing import Any, List, Optional, Tuple, Union

from eth_abi.abi import decode

from .exceptions import CONSTRUCTOR_NOT_FOUND, INVALID_INPUT, METHOD_NOT_FOUND
from .utils import (
    detect_constructor_arguments,
    get_constructor_type,
    get_selector_to_function_type,
    get_types_names,
    hex_to_bytes,
)


@dataclass(frozen=True)
class ContractCall:
    name: str
    arguments: List[Tuple[str, str, Any]]


class InputDecoder:
    def __init__(self, abi: List[dict]):
        self._constructor_type = get_constructor_type(abi)
        self._selector_to_func_type = get_selector_to_function_type(abi)

    def decode_function(self, tx_input: Union[str, bytes]):
        tx_input = hex_to_bytes(tx_input)
        selector, args = tx_input[:4], tx_input[4:]
        type_def = self._selector_to_func_type.get(selector, None)
        if not type_def:
            raise METHOD_NOT_FOUND

        types, names = get_types_names(type_def["inputs"])

        try:
            values = decode(types, args)
        except OverflowError:
            raise INVALID_INPUT

        return ContractCall(type_def["name"], list(zip(types, names, values)))

    def decode_constructor(
        self,
        tx_input: Union[str, bytes],
        bytecode: Optional[Union[str, bytes]] = None,
    ):
        tx_input = hex_to_bytes(tx_input)

        if not self._constructor_type:
            raise CONSTRUCTOR_NOT_FOUND

        if bytecode is not None:
            bytecode_len = len(hex_to_bytes(bytecode))
            tx_input = tx_input[bytecode_len:]
        else:
            tx_input = detect_constructor_arguments(self._constructor_type, tx_input)

        types, names = get_types_names(self._constructor_type["inputs"])
        values = decode(types, tx_input)

        return ContractCall("constructor", list(zip(types, names, values)))
