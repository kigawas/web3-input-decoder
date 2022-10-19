from web3_input_decoder import decode_constructor, decode_function

from .data.caller import (
    CALLER_CONSTRUCTOR_CALL_ARGUMENT,
    CALLER_CONSTRUCTOR_CALL_INPUT,
    CALLER_CONTRACT_ABI,
)
from .data.defi import ROUTER_ABI, ROUTER_SWAP_CALL_ARGUMENT, ROUTER_SWAP_CALL_INPUT
from .data.example import (
    EXAMPLE_CONSTRUCTOR_CALL_ARGUMENT,
    EXAMPLE_CONSTRUCTOR_CALL_INPUT,
    EXAMPLE_CONTRACT_ABI,
    EXAMPLE_CONTRACT_BYTECODE,
)
from .data.nft import (
    SEAPORT_ABI,
    SEAPORT_FULFILL_ORDER_CALL_ARGUMENT,
    SEAPORT_FULFILL_ORDER_CALL_INPUT,
)
from .data.tether import (
    TETHER_ABI,
    TETHER_BYTECODE,
    TETHER_CONSTRUCTOR_ARGS,
    TETHER_CONSTRUCTOR_TX_INPUT,
    TETHER_CONSTRUCTOR_TX_INPUT_WITH_BYTECODE,
)


def test_decode_function():
    tether_input = (
        "0xa9059cbb000000000000000000000000f050227be1a7ce587aa83d5013f900dbc3b"
        "e0611000000000000000000000000000000000000000000000000000000000ecdd350"
    )
    tether_args = [
        ("address", "_to", "0xf050227be1a7ce587aa83d5013f900dbc3be0611"),
        ("uint256", "_value", 248370000),
    ]

    abis = [
        TETHER_ABI,
        ROUTER_ABI,
        SEAPORT_ABI,
    ]
    inputs = [
        tether_input,
        ROUTER_SWAP_CALL_INPUT,
        SEAPORT_FULFILL_ORDER_CALL_INPUT,
    ]
    expected_args = [
        tether_args,
        ROUTER_SWAP_CALL_ARGUMENT,
        SEAPORT_FULFILL_ORDER_CALL_ARGUMENT,
    ]

    for abi, input, expected in zip(abis, inputs, expected_args):
        assert decode_function(abi, input) == expected


def test_decode_constructor():
    abis = [TETHER_ABI, CALLER_CONTRACT_ABI]
    inputs = [TETHER_CONSTRUCTOR_TX_INPUT, CALLER_CONSTRUCTOR_CALL_INPUT]
    expected_args = [TETHER_CONSTRUCTOR_ARGS, CALLER_CONSTRUCTOR_CALL_ARGUMENT]
    for abi, input, expected in zip(abis, inputs, expected_args):
        assert decode_constructor(abi, input) == expected


def test_decode_constructor_with_bytecode():
    abis = [
        TETHER_ABI,
        EXAMPLE_CONTRACT_ABI,
    ]
    inputs = [
        TETHER_CONSTRUCTOR_TX_INPUT_WITH_BYTECODE,
        EXAMPLE_CONSTRUCTOR_CALL_INPUT,
    ]
    bytecodes = [
        TETHER_BYTECODE,
        EXAMPLE_CONTRACT_BYTECODE,
    ]
    expected_args = [
        TETHER_CONSTRUCTOR_ARGS,
        EXAMPLE_CONSTRUCTOR_CALL_ARGUMENT,
    ]
    for abi, input, bytecode, expected in zip(abis, inputs, bytecodes, expected_args):
        assert decode_constructor(abi, input, bytecode) == expected
