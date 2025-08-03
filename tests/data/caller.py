from __future__ import annotations

from web3_input_decoder.types import Abi

# Made with Remix IDE

"""
// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract Caller {
    address addr;

    constructor(address _addr) {
        addr = _addr;
    }
}
"""

CALLER_ABI: Abi = [
    {
        "inputs": [{"internalType": "address", "name": "_addr", "type": "address"}],
        "stateMutability": "nonpayable",
        "type": "constructor",
    }
]


CALLER_CONSTRUCTOR_CALL_INPUT_WITHOUT_BYTECODE = (
    "0x0000000000000000000000000000000000000000000000000000000000000002"
)

CALLER_CONSTRUCTOR_CALL_ARGUMENT = [
    ("address", "_addr", "0x0000000000000000000000000000000000000002")
]
