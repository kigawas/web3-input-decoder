import pytest
from pyinstrument import Profiler

from web3_input_decoder import InputDecoder

from .data.tether import TETHER_ABI


@pytest.mark.parametrize(
    "count",
    [10, 100, 1000, 10000],
)
def test_profiling_tether_transfer_decode(count: int):
    p = Profiler()
    tx = (
        "0xa9059cbb000000000000000000000000f050227be1a7ce587aa83d5013f900dbc3b"
        "e0611000000000000000000000000000000000000000000000000000000000ecdd350"
    )
    with p:
        decoder = InputDecoder(TETHER_ABI)
        for _ in range(count):
            func_call = decoder.decode_function(tx)
            assert func_call.name == "transfer"
    p.print()
