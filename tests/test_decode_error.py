import pytest

from web3_input_decoder import decode_constructor, decode_function
from web3_input_decoder.exceptions import InputDataError

from .data.example import EXAMPLE_CONSTRUCTOR_CALL_INPUT, EXAMPLE_CONTRACT_ABI
from .data.tether import TETHER_ABI


def test_decode_constructor_error():
    with pytest.raises(
        InputDataError, match="Unable to detect arguments including array"
    ):
        decode_constructor(EXAMPLE_CONTRACT_ABI, EXAMPLE_CONSTRUCTOR_CALL_INPUT)

    with pytest.raises(InputDataError, match="Constructor is not found in ABI"):
        decode_constructor([{"type": "function", "name": "test"}], "0x00")


def test_decode_function_error():
    with pytest.raises(InputDataError, match="Specified method is not found in ABI"):
        decode_function(TETHER_ABI, "0x00000000")

    with pytest.raises(InputDataError, match="Specified method is not found in ABI"):
        decode_function([{"type": "function", "name": "test"}], "0x00")
