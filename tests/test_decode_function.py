import pytest

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
    TETHER_TRANSFER_CALL_ARGUMENT,
    TETHER_TRANSFER_CALL_INPUT,
)


@pytest.mark.parametrize(
    "abi,input,expected",
    [
        (TETHER_ABI, TETHER_TRANSFER_CALL_INPUT, TETHER_TRANSFER_CALL_ARGUMENT),
        (ROUTER_ABI, ROUTER_SWAP_CALL_INPUT, ROUTER_SWAP_CALL_ARGUMENT),
        (ROUTER_ABI, ROUTER_TOKENS_SWAP_CALL_INPUT, ROUTER_TOKENS_SWAP_CALL_ARGUMENT),
        (
            SEAPORT_ABI,
            SEAPORT_FULFILL_ORDER_CALL_INPUT,
            SEAPORT_FULFILL_ORDER_CALL_ARGUMENT,
        ),
    ],
    ids=["tether", "router-swap", "router-tokens-swap", "seaport-fulfill-order"],
)
def test_decode_function(abi, input, expected):
    assert decode_function(abi, input) == expected
