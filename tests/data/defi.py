ROUTER_ABI = [
    {
        "name": "swapExactAVAXForTokens",
        "type": "function",
        "inputs": [
            {"name": "amountOutMin", "type": "uint256"},
            {"name": "path", "type": "address[]"},
            {"name": "to", "type": "address"},
            {"name": "deadline", "type": "uint256"},
        ],
        "outputs": [{"name": "amounts", "type": "uint256[]"}],
    }
]

ROUTER_SWAP_CALL_INPUT = "0xa2a1623d000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000800000000000000000000000006ef4158bf7304b966929945248927fb400ece8b500000000000000000000000000000000000000000000000000000000622bc5e10000000000000000000000000000000000000000000000000000000000000002000000000000000000000000b31f66aa3c1e785363f0875a1b74e27b85fd66c70000000000000000000000003df307e8e9a897da488211682430776cdf0f17cc"
ROUTER_SWAP_CALL_ARGUMENT = [
    ("uint256", "amountOutMin", 0),
    (
        "address[]",
        "path",
        (
            "0xb31f66aa3c1e785363f0875a1b74e27b85fd66c7",
            "0x3df307e8e9a897da488211682430776cdf0f17cc",
        ),
    ),
    ("address", "to", "0x6ef4158bf7304b966929945248927fb400ece8b5"),
    ("uint256", "deadline", 1647035873),
]
