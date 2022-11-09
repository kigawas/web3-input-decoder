from web3_input_decoder import decode_constructor

from .data.caller import (
    CALLER_CONSTRUCTOR_CALL_ARGUMENT,
    CALLER_CONSTRUCTOR_CALL_INPUT,
    CALLER_CONTRACT_ABI,
)
from .data.example import (
    EXAMPLE_CONSTRUCTOR_CALL_ARGUMENT,
    EXAMPLE_CONSTRUCTOR_CALL_INPUT,
    EXAMPLE_CONTRACT_ABI,
    EXAMPLE_CONTRACT_BYTECODE,
)
from .data.tether import (
    TETHER_ABI,
    TETHER_BYTECODE,
    TETHER_CONSTRUCTOR_ARGS,
    TETHER_CONSTRUCTOR_TX_INPUT,
    TETHER_CONSTRUCTOR_TX_INPUT_WITH_BYTECODE,
)


def test_decode_constructor():
    abis = [TETHER_ABI, CALLER_CONTRACT_ABI]
    inputs = [TETHER_CONSTRUCTOR_TX_INPUT, CALLER_CONSTRUCTOR_CALL_INPUT]
    expected_args = [TETHER_CONSTRUCTOR_ARGS, CALLER_CONSTRUCTOR_CALL_ARGUMENT]

    for abi, input, expected in zip(abis, inputs, expected_args):
        assert decode_constructor(abi, input) == expected


def test_decode_constructor_with_bytecode():
    abis = [TETHER_ABI, EXAMPLE_CONTRACT_ABI]
    inputs = [TETHER_CONSTRUCTOR_TX_INPUT_WITH_BYTECODE, EXAMPLE_CONSTRUCTOR_CALL_INPUT]
    bytecodes = [TETHER_BYTECODE, EXAMPLE_CONTRACT_BYTECODE]
    expected_args = [TETHER_CONSTRUCTOR_ARGS, EXAMPLE_CONSTRUCTOR_CALL_ARGUMENT]

    for abi, input, bytecode, expected in zip(abis, inputs, bytecodes, expected_args):
        assert decode_constructor(abi, input, bytecode) == expected
