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


def test_decode_constructor_without_bytecode():
    abis = [TETHER_ABI, CALLER_ABI]
    inputs = [
        TETHER_CONSTRUCTOR_CALL_INPUT_WITHOUT_BYTECODE,
        CALLER_CONSTRUCTOR_CALL_INPUT_WITHOUT_BYTECODE,
    ]
    expected_args = [TETHER_CONSTRUCTOR_CALL_ARGUMENT, CALLER_CONSTRUCTOR_CALL_ARGUMENT]

    for abi, input, expected in zip(abis, inputs, expected_args):
        assert decode_constructor(abi, input) == expected


def test_decode_constructor_with_bytecode():
    abis = [TETHER_ABI, EXAMPLE_ABI, STORAGE_ABI]
    inputs = [
        TETHER_CONSTRUCTOR_CALL_INPUT,
        EXAMPLE_CONSTRUCTOR_CALL_INPUT,
        STORAGE_CONSTRUCTOR_CALL_INPUT,
    ]
    bytecodes = [TETHER_BYTECODE, EXAMPLE_BYTECODE, STORAGE_BYTECODE]
    expected_args = [
        TETHER_CONSTRUCTOR_CALL_ARGUMENT,
        EXAMPLE_CONSTRUCTOR_CALL_ARGUMENT,
        STORAGE_CONSTRUCTOR_CALL_ARGUMENT,
    ]

    for abi, input, bytecode, expected in zip(abis, inputs, bytecodes, expected_args):
        assert decode_constructor(abi, input, bytecode) == expected
