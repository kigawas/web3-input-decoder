import pytest
from pyinstrument import Profiler

from web3_input_decoder import InputDecoder

from .data.defi import ROUTER_ABI, ROUTER_TOKENS_SWAP_CALL_INPUT
from .data.tether import TETHER_ABI


@pytest.mark.parametrize(
    "count",
    [10, 100, 1000, 10000],
)
def test_profiling_tether_transfer_decode(count: int):
    tx = (
        "0xa9059cbb000000000000000000000000f050227be1a7ce587aa83d5013f900dbc3b"
        "e0611000000000000000000000000000000000000000000000000000000000ecdd350"
    )
    __check(TETHER_ABI, tx, "transfer", count)


@pytest.mark.parametrize(
    "count",
    [10, 100, 1000, 10000],
)
def test_profiling_router_swap(count: int):
    __check(
        ROUTER_ABI,
        ROUTER_TOKENS_SWAP_CALL_INPUT,
        "swapExactTokensForTokens",
        count,
    )


def __check(abi, tx: str, func_name: str, count: int):
    p = Profiler()
    with p:
        decoder = InputDecoder(abi)
        for _ in range(count):
            func_call = decoder.decode_function(tx)
            assert func_call.name == func_name
    p.print()
