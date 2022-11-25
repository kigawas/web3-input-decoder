import pytest

from web3_input_decoder.utils import (
    detect_constructor_arguments,
    get_constructor_type,
    get_selector_to_function_type,
    hex_to_bytes,
)

from .data.tether import (
    TETHER_ABI,
    TETHER_CONSTRUCTOR_CALL_INPUT,
    TETHER_CONSTRUCTOR_CALL_INPUT_WITHOUT_BYTECODE,
)


@pytest.mark.parametrize(
    "abi,input_with_bytecode,input",
    [
        (
            TETHER_ABI,
            TETHER_CONSTRUCTOR_CALL_INPUT,
            TETHER_CONSTRUCTOR_CALL_INPUT_WITHOUT_BYTECODE,
        ),
        (
            TETHER_ABI,
            TETHER_CONSTRUCTOR_CALL_INPUT_WITHOUT_BYTECODE,
            TETHER_CONSTRUCTOR_CALL_INPUT_WITHOUT_BYTECODE,
        ),
    ],
)
def test_detect_arguments(abi, input_with_bytecode, input):
    assert detect_constructor_arguments(
        get_constructor_type(abi), hex_to_bytes(input_with_bytecode)
    ) == hex_to_bytes(input)


def test_selector_to_func_type():
    assert get_selector_to_function_type(TETHER_ABI) != {}
