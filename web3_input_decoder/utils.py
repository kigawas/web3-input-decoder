from typing import Any, List, Tuple, Union

from eth_abi.abi import encode_abi

__all__ = (
    "get_constructor_type",
    "get_types_names",
    "hex_to_bytes",
    "detect_constructor_arguments",
)


def get_constructor_type(abi: List[dict]) -> dict:
    for type_def in abi:
        if type_def["type"] == "constructor":
            return type_def
    raise NotImplementedError("constructor is not available")


def get_types_names(type_def: dict) -> Tuple[List[str], List[str]]:
    types = [t["type"] for t in type_def]
    names = [t["name"] for t in type_def]
    return types, names


def hex_to_bytes(data: Union[str, bytes]) -> bytes:
    if isinstance(data, str):
        if data.startswith("0x"):
            data = data[2:]
        data = bytes.fromhex(data)
    return data


def detect_constructor_arguments(
    abi: List[dict],
    tx_input_with_bytecode: Union[str, bytes],
) -> bytes:
    type_def = get_constructor_type(abi)["inputs"]
    types, _ = get_types_names(type_def)
    default_values: List[Any] = []
    for t in types:
        if "int" in t:
            default_values.append(0)
        elif "[]" in t:
            raise ValueError(
                "Unable to detect arguments including array. "
                "Please provide the bytecode."
            )
        elif "string" == t:
            default_values.append("")
        elif "bool" == t:
            default_values.append(False)
        elif "address" == t:
            default_values.append("0x0000000000000000000000000000000000000000")
        else:
            raise NotImplementedError(f"Type {t} is not implemented yet")

    default_args = encode_abi(types, default_values)
    return hex_to_bytes(tx_input_with_bytecode)[-len(default_args) :]
