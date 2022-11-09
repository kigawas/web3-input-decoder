from web3_input_decoder import decode_function

from .data.defi import (
    ROUTER_ABI,
    ROUTER_SWAP_CALL_ARGUMENT,
    ROUTER_SWAP_CALL_INPUT,
    ROUTER_TOKENS_SWAP_CALL_ARGUMENT,
    ROUTER_TOKENS_SWAP_CALL_INPUT,
)
from .data.nft import (
    SEAPORT_ABI,
    SEAPORT_FULFILL_ORDER_CALL_ARGUMENT,
    SEAPORT_FULFILL_ORDER_CALL_INPUT,
)
from .data.tether import (
    TETHER_ABI,
    THTHER_TRANSFER_CALL_ARGUMENT,
    THTHER_TRANSFER_CALL_INPUT,
)


def test_decode_function():
    abis = [TETHER_ABI, ROUTER_ABI, ROUTER_ABI, SEAPORT_ABI]
    inputs = [
        THTHER_TRANSFER_CALL_INPUT,
        ROUTER_SWAP_CALL_INPUT,
        ROUTER_TOKENS_SWAP_CALL_INPUT,
        SEAPORT_FULFILL_ORDER_CALL_INPUT,
    ]
    expected_args = [
        THTHER_TRANSFER_CALL_ARGUMENT,
        ROUTER_SWAP_CALL_ARGUMENT,
        ROUTER_TOKENS_SWAP_CALL_ARGUMENT,
        SEAPORT_FULFILL_ORDER_CALL_ARGUMENT,
    ]

    for abi, input, expected in zip(abis, inputs, expected_args):
        assert decode_function(abi, input) == expected
