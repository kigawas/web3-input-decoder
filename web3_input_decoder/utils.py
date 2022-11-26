from typing import Any, List, Tuple, Union

from eth_abi.abi import encode
from eth_utils.abi import function_abi_to_4byte_selector

from .exceptions import UNABLE_TO_DETECT_CONSTRUCTOR_ARGUMENTS

__all__ = (
    "get_constructor_type",
    "get_selector_to_function_type",
    "get_types_names",
    "expand_tuple_types",
    "hex_to_bytes",
    "detect_constructor_arguments",
)


def get_constructor_type(abi: List[dict]) -> dict:
    for type_def in abi:
        if type_def["type"] == "constructor":
            return type_def
    return {}


def get_selector_to_function_type(abi: List[dict]) -> dict:
    type_defs = {}
    for type_def in abi:
        if type_def["type"] == "function":
            selector = function_abi_to_4byte_selector(type_def)
            type_defs[selector] = type_def
    return type_defs


def expand_tuple_types(type_def: dict) -> str:
    types = []
    for comp in type_def["components"]:
        if "components" not in comp:
            types.append(comp["type"])
        else:
            types.append(expand_tuple_types(comp))
    types_str = ",".join(types)
    return f"({types_str})"


def get_types_names(inputs: List[dict]) -> Tuple[List[str], List[str]]:
    types = []
    for t in inputs:
        if t["type"] == "tuple":
            types.append(expand_tuple_types(t))
        elif t["type"] == "tuple[]":
            types.append(f"{expand_tuple_types(t)}[]")
        else:
            types.append(t["type"])

    names = [t["name"] for t in inputs]
    return types, names


def hex_to_bytes(data: Union[str, bytes]) -> bytes:
    if isinstance(data, str):
        if data.startswith("0x"):
            data = data[2:]
        data = bytes.fromhex(data)
    return data


def detect_constructor_arguments(
    type_def: dict,
    tx_input_with_bytecode: Union[str, bytes],
) -> bytes:
    types, _ = get_types_names(type_def["inputs"])
    default_values: List[Any] = []
    for t in types:
        if t.endswith("[]"):
            raise UNABLE_TO_DETECT_CONSTRUCTOR_ARGUMENTS
        elif "int" in t:
            default_values.append(0)
        elif "string" == t:
            default_values.append("0")
        elif "bool" == t:
            default_values.append(False)
        elif "address" == t:
            default_values.append("0x0000000000000000000000000000000000000000")
        else:
            raise NotImplementedError(f"Type {t} is not implemented yet")

    default_args = encode(types, default_values)
    return hex_to_bytes(tx_input_with_bytecode)[-len(default_args) :]
