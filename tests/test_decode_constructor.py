import pytest

from web3_input_decoder import decode_constructor

from .data.caller import (
    CALLER_ABI,
    CALLER_CONSTRUCTOR_CALL_ARGUMENT,
    CALLER_CONSTRUCTOR_CALL_INPUT_WITHOUT_BYTECODE,
)
from .data.example import (
    EXAMPLE_ABI,
    EXAMPLE_BYTECODE,
    EXAMPLE_CONSTRUCTOR_CALL_ARGUMENT,
    EXAMPLE_CONSTRUCTOR_CALL_INPUT,
    EXAMPLE_CONSTRUCTOR_CALL_INPUT_WITHOUT_BYTECODE,
)
from .data.storage import (
    STORAGE_ABI,
    STORAGE_BYTECODE,
    STORAGE_CONSTRUCTOR_CALL_ARGUMENT,
    STORAGE_CONSTRUCTOR_CALL_INPUT,
)
from .data.tether import (
    TETHER_ABI,
    TETHER_BYTECODE,
    TETHER_CONSTRUCTOR_CALL_ARGUMENT,
    TETHER_CONSTRUCTOR_CALL_INPUT,
    TETHER_CONSTRUCTOR_CALL_INPUT_WITHOUT_BYTECODE,
)


@pytest.mark.parametrize(
    "abi,input,expected",
    [
        (
            TETHER_ABI,
            TETHER_CONSTRUCTOR_CALL_INPUT_WITHOUT_BYTECODE,
            TETHER_CONSTRUCTOR_CALL_ARGUMENT,
        ),
        (
            CALLER_ABI,
            CALLER_CONSTRUCTOR_CALL_INPUT_WITHOUT_BYTECODE,
            CALLER_CONSTRUCTOR_CALL_ARGUMENT,
        ),
        (
            EXAMPLE_ABI,
            EXAMPLE_CONSTRUCTOR_CALL_INPUT_WITHOUT_BYTECODE,
            EXAMPLE_CONSTRUCTOR_CALL_ARGUMENT,
        ),
    ],
    ids=["tether", "caller", "example"],
)
def test_decode_constructor_without_bytecode(abi, input, expected):
    assert decode_constructor(abi, input) == expected


@pytest.mark.parametrize(
    "abi,input,bytecode,expected",
    [
        (
            TETHER_ABI,
            TETHER_CONSTRUCTOR_CALL_INPUT,
            TETHER_BYTECODE,
            TETHER_CONSTRUCTOR_CALL_ARGUMENT,
        ),
        (
            EXAMPLE_ABI,
            EXAMPLE_CONSTRUCTOR_CALL_INPUT,
            EXAMPLE_BYTECODE,
            EXAMPLE_CONSTRUCTOR_CALL_ARGUMENT,
        ),
        (
            STORAGE_ABI,
            STORAGE_CONSTRUCTOR_CALL_INPUT,
            STORAGE_BYTECODE,
            STORAGE_CONSTRUCTOR_CALL_ARGUMENT,
        ),
    ],
    ids=["tether", "example", "storage"],
)
def test_decode_constructor_with_bytecode(abi, input, bytecode, expected):
    assert decode_constructor(abi, input, bytecode) == expected
