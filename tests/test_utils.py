from web3_input_decoder.utils import (
    detect_constructor_arguments,
    get_constructor_type,
    hex_to_bytes,
)

from .data.tether import (
    TETHER_ABI,
    TETHER_CONSTRUCTOR_TX_INPUT,
    TETHER_CONSTRUCTOR_TX_INPUT_WITH_BYTECODE,
)


def test_detect_arguments():
    constructor_type_def = get_constructor_type(TETHER_ABI)
    assert detect_constructor_arguments(
        constructor_type_def,
        hex_to_bytes(TETHER_CONSTRUCTOR_TX_INPUT_WITH_BYTECODE),
    ) == hex_to_bytes(TETHER_CONSTRUCTOR_TX_INPUT)
    assert detect_constructor_arguments(
        constructor_type_def,
        hex_to_bytes(TETHER_CONSTRUCTOR_TX_INPUT),
    ) == hex_to_bytes(TETHER_CONSTRUCTOR_TX_INPUT)
