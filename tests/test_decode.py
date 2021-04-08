import pytest

from web3_input_decoder import decode_constructor, decode_function
from web3_input_decoder.exceptions import InputDataError
from web3_input_decoder.utils import get_constructor_type

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


def test_decode_function():
    assert decode_function(
        TETHER_ABI,
        (
            "0xa9059cbb000000000000000000000000f050227be1a7ce587aa83d5013f900dbc3be"
            "0611000000000000000000000000000000000000000000000000000000000ecdd350"
        ),
    ) == [
        ("address", "_to", "0xf050227be1a7ce587aa83d5013f900dbc3be0611"),
        ("uint256", "_value", 248370000),
    ]

    with pytest.raises(InputDataError):
        decode_function(TETHER_ABI, "0x00000000")


def test_decode_constructor():
    assert (
        decode_constructor(TETHER_ABI, TETHER_CONSTRUCTOR_TX_INPUT)
        == TETHER_CONSTRUCTOR_ARGS
    )

    assert (
        decode_constructor(
            TETHER_ABI,
            TETHER_CONSTRUCTOR_TX_INPUT_WITH_BYTECODE,
            TETHER_BYTECODE,
        )
        == TETHER_CONSTRUCTOR_ARGS
    )

    assert (
        decode_constructor(
            EXAMPLE_CONTRACT_ABI,
            EXAMPLE_CONSTRUCTOR_CALL_INPUT,
            EXAMPLE_CONTRACT_BYTECODE,
        )
        == EXAMPLE_CONSTRUCTOR_CALL_ARGUMENT
    )
    assert (
        decode_constructor(
            CALLER_CONTRACT_ABI,
            CALLER_CONSTRUCTOR_CALL_INPUT,
        )
        == CALLER_CONSTRUCTOR_CALL_ARGUMENT
    )

    with pytest.raises(InputDataError):
        decode_constructor(EXAMPLE_CONTRACT_ABI, EXAMPLE_CONSTRUCTOR_CALL_INPUT)

    with pytest.raises(InputDataError):
        get_constructor_type([{"type": "function"}])
