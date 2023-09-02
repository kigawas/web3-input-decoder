from typing import List, Literal, TypedDict


class Input(TypedDict):
    name: str
    type: str
    components: List["Input"]


class TypeDef(TypedDict):
    name: str
    type: Literal["constructor", "function"]
    inputs: List[Input]


Abi = List[TypeDef]
