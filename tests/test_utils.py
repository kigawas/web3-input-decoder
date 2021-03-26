from web3_input_decoder.utils import detect_constructor_arguments, hex_to_bytes

from .data.tether import (
    TETHER_ABI,
    TETHER_CONSTRUCTOR_TX_INPUT,
    TETHER_CONSTRUCTOR_TX_INPUT_WITH_BYTECODE,
)


def test_detect_arguments():
    assert (
        detect_constructor_arguments(
            TETHER_ABI,
            hex_to_bytes(TETHER_CONSTRUCTOR_TX_INPUT_WITH_BYTECODE),
        )
        == hex_to_bytes(TETHER_CONSTRUCTOR_TX_INPUT)
    )
    assert (
        detect_constructor_arguments(
            TETHER_ABI,
            hex_to_bytes(TETHER_CONSTRUCTOR_TX_INPUT),
        )
        == hex_to_bytes(TETHER_CONSTRUCTOR_TX_INPUT)
    )
