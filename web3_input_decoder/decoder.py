from dataclasses import dataclass
from typing import Any, List, Optional, Tuple, Union

from eth_abi.exceptions import DecodingError

from .exceptions import (
    CONSTRUCTOR_NOT_FOUND,
    INVALID_INPUT,
    METHOD_NOT_FOUND,
    InputDataError,
)
from .types import Abi, Input
from .utils import (
    decode_input,
    detect_constructor_arguments,
    get_constructor_type,
    get_selector_to_function_type,
    hex_to_bytes,
)

__all__ = (
    "ContractCall",
    "InputDecoder",
)


@dataclass(frozen=True)
class ContractCall:
    name: str
    arguments: List[Tuple[str, str, Any]]

    @classmethod
    def decode(cls, func_name: str, inputs: List[Input], func_args: bytes):
        try:
            types, names, values = decode_input(inputs, func_args)
            return cls(func_name, list(zip(types, names, values)))
        except (DecodingError, OverflowError):
            raise INVALID_INPUT


class InputDecoder:
    __slots__ = ["_constructor_type", "_selector_to_func_type"]

    def __init__(self, abi: Abi):
        self._constructor_type = get_constructor_type(abi)
        self._selector_to_func_type = get_selector_to_function_type(abi)

    def decode_function(self, tx_input: Union[str, bytes]):
        tx_input = hex_to_bytes(tx_input)
        selector, func_args = tx_input[:4], tx_input[4:]
        type_def = self._selector_to_func_type.get(selector, None)
        if not type_def:
            raise METHOD_NOT_FOUND

        return ContractCall.decode(type_def["name"], type_def["inputs"], func_args)

    def decode_constructor(
        self,
        tx_input: Union[str, bytes],
        bytecode: Optional[Union[str, bytes]] = None,
    ):
        tx_input = hex_to_bytes(tx_input)
        if not self._constructor_type:
            raise CONSTRUCTOR_NOT_FOUND

        func_name = "constructor"
        inputs = self._constructor_type["inputs"]

        if bytecode is not None:
            # bytecode is provided => assuming tx input has bytecode
            func_args = tx_input[len(hex_to_bytes(bytecode)) :]
        else:
            try:
                # if tx_input has no bytecode, it may just succeed
                return ContractCall.decode(func_name, inputs, tx_input)
            except (DecodingError, InputDataError):
                # tx input has bytecode and bytecode is not provided => detect
                pass

            func_args = detect_constructor_arguments(self._constructor_type, tx_input)

        return ContractCall.decode(func_name, inputs, func_args)
