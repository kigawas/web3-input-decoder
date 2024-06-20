from typing import Any, Dict, List, Optional, Tuple

from eth_abi.abi import decode, encode
from eth_utils.abi import function_abi_to_4byte_selector

from ..exceptions import UNABLE_TO_DETECT_CONSTRUCTOR_ARGUMENTS
from ..types import Abi, Input, TypeDef


def get_constructor_type(abi: Abi) -> Optional[TypeDef]:
    for type_def in abi:
        if type_def["type"] == "constructor":
            return type_def
    return None


def get_selector_to_function_type(abi: Abi) -> Dict[bytes, TypeDef]:
    type_defs = {}
    for type_def in abi:
        if type_def["type"] == "function":
            selector = function_abi_to_4byte_selector(type_def)  # type:ignore[arg-type]
            type_defs[selector] = type_def
    return type_defs


def detect_constructor_arguments(type_def: TypeDef, data_with_bytecode: bytes):
    inputs = type_def["inputs"]  # TODO: remove this from 0.2.0
    has_array, default_args = get_default_arguments(inputs)
    if has_array:
        raise UNABLE_TO_DETECT_CONSTRUCTOR_ARGUMENTS
    return data_with_bytecode[-len(default_args) :]


def get_default_arguments(inputs: List[Input]):
    types, _ = get_types_names(inputs)
    default_values: List[Any] = []
    has_array = False
    for t in types:
        if t.endswith("[]"):
            default_values.append([])
            has_array = True
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

    return has_array, encode(types, default_values)


def decode_input(inputs: List[Input], func_args: bytes):
    types, names = get_types_names(inputs)
    values = decode(types, func_args)
    return types, names, values


def get_types_names(inputs: List[Input]) -> Tuple[List[str], List[str]]:
    types = []
    for t in inputs:
        if t["type"] == "tuple":
            types.append(__expand_tuple_types(t))
        elif t["type"] == "tuple[]":
            types.append(f"{__expand_tuple_types(t)}[]")
        else:
            types.append(t["type"])

    names = [t["name"] for t in inputs]
    return types, names


def __expand_tuple_types(input: Input) -> str:
    types = []
    for comp in input["components"]:
        if "components" not in comp:
            types.append(comp["type"])
        elif comp["type"] == "tuple[]":
            types.append(f"{__expand_tuple_types(comp)}[]")
        else:
            types.append(__expand_tuple_types(comp))
    types_str = ",".join(types)
    return f"({types_str})"
