import pytest

from web3_input_decoder import decode_constructor, decode_function
from web3_input_decoder.exceptions import InputDataError

from .data.example import EXAMPLE_CONSTRUCTOR_CALL_INPUT, EXAMPLE_CONTRACT_ABI
from .data.tether import TETHER_ABI

INVALID_ABI = [{"type": "function", "name": "test"}]
UNABLE_TO_DETECT = "Unable to detect arguments including array"
CONSTRUCTOR_NOT_FOUND = "Constructor is not found in ABI"
METHOD_NOT_FOUND = "Specified method is not found in ABI"


@pytest.mark.parametrize(
    "abi,input,match",
    zip(
        [EXAMPLE_CONTRACT_ABI, INVALID_ABI],
        [EXAMPLE_CONSTRUCTOR_CALL_INPUT, "0x00"],
        [UNABLE_TO_DETECT, CONSTRUCTOR_NOT_FOUND],
    ),
)
def test_decode_constructor_error(abi, input, match):
    with pytest.raises(InputDataError, match=match):
        decode_constructor(abi, input)


@pytest.mark.parametrize(
    "abi,input,match",
    zip(
        [TETHER_ABI, INVALID_ABI],
        ["0x00000000", "0x00"],
        [METHOD_NOT_FOUND, METHOD_NOT_FOUND],
    ),
)
def test_decode_function_error(abi, input, match):
    with pytest.raises(InputDataError, match=match):
        decode_function(abi, input)
