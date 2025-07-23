from __future__ import annotations

import sys
from typing import Literal, Union

if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict


class Input(TypedDict):
    name: str
    type: str
    components: NotRequired[list[Input]]  # only for "tuple" and "tuple[]"
    internalType: NotRequired[str]


class Output(TypedDict):
    name: str
    type: str
    components: NotRequired[list[Output]]  # only for "tuple" and "tuple[]"
    internalType: NotRequired[str]


class ConstructorType(TypedDict):
    name: NotRequired[str]
    type: Literal["constructor"]
    inputs: list[Input]
    constant: NotRequired[bool]
    payable: NotRequired[bool]
    stateMutability: NotRequired[Literal["pure", "view", "nonpayable", "payable"]]


class FunctionType(TypedDict):
    name: str
    type: Literal["function"]
    inputs: list[Input]
    constant: NotRequired[bool]
    payable: NotRequired[bool]
    stateMutability: NotRequired[Literal["pure", "view", "nonpayable", "payable"]]
    outputs: NotRequired[list[Output]]


TypeDef = Union[ConstructorType, FunctionType]  # for backward compatibility
Abi = list[TypeDef]
