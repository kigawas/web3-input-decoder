import pytest

from web3_input_decoder import decode_constructor, decode_function
from web3_input_decoder.exceptions import InputDataError

from .data.defi import ROUTER_V2_ABI, ROUTER_V2_TOKENS_SWAP_CALL_ERROR_INPUT
from .data.example import EXAMPLE_ABI, EXAMPLE_CONSTRUCTOR_CALL_INPUT
from .data.storage import STORAGE_ABI, STORAGE_CONSTRUCTOR_CALL_INPUT
from .data.tether import TETHER_ABI

INVALID_ABI = [{"inputs": [], "type": "function", "name": "test"}]
INVALID_CALL_INPUT = "0x00"

UNABLE_TO_DETECT = "Unable to detect arguments including array"
CONSTRUCTOR_NOT_FOUND = "Constructor is not found in ABI"
METHOD_NOT_FOUND = "Specified method is not found in ABI"
INVALID_INPUT = "Invalid input"


@pytest.mark.parametrize(
    "abi,input,match",
    [
        (INVALID_ABI, INVALID_CALL_INPUT, CONSTRUCTOR_NOT_FOUND),
        (EXAMPLE_ABI, EXAMPLE_CONSTRUCTOR_CALL_INPUT, UNABLE_TO_DETECT),
        (STORAGE_ABI, STORAGE_CONSTRUCTOR_CALL_INPUT, UNABLE_TO_DETECT),
    ],
)
def test_decode_constructor_error(abi, input, match):
    with pytest.raises(InputDataError, match=match):
        decode_constructor(abi, input)


@pytest.mark.parametrize(
    "abi,input,match",
    [
        (TETHER_ABI, INVALID_CALL_INPUT, METHOD_NOT_FOUND),
        (INVALID_ABI, INVALID_CALL_INPUT, METHOD_NOT_FOUND),
        (ROUTER_V2_ABI, ROUTER_V2_TOKENS_SWAP_CALL_ERROR_INPUT, INVALID_INPUT),
    ],
)
def test_decode_function_error(abi, input, match):
    with pytest.raises(InputDataError, match=match):
        decode_function(abi, input)
