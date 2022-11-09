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
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "amountIn", "type": "uint256"},
            {"internalType": "uint256", "name": "amountOutMin", "type": "uint256"},
            {
                "components": [
                    {"internalType": "address", "name": "from", "type": "address"},
                    {"internalType": "address", "name": "to", "type": "address"},
                    {"internalType": "bool", "name": "stable", "type": "bool"},
                ],
                "internalType": "struct BaseV1Router01.route[]",
                "name": "routes",
                "type": "tuple[]",
            },
            {"internalType": "address", "name": "to", "type": "address"},
            {"internalType": "uint256", "name": "deadline", "type": "uint256"},
        ],
        "name": "swapExactTokensForTokens",
        "outputs": [
            {"internalType": "uint256[]", "name": "amounts", "type": "uint256[]"}
        ],
        "stateMutability": "nonpayable",
        "type": "function",
    },
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

ROUTER_TOKENS_SWAP_CALL_INPUT = "0xf41766d80000000000000000000000000000000000000000000000000000000002dc6c000000000000000000000000000000000000000000000000001bbc2e22c5c1c2cb00000000000000000000000000000000000000000000000000000000000000a00000000000000000000000007c77b132a0cd0ad1c694ab8645affa26c2787d6600000000000000000000000000000000000000000000000000000000636aaa2f0000000000000000000000000000000000000000000000000000000000000001000000000000000000000000ea32a96608495e54156ae48931a7c20f0dcc1a21000000000000000000000000deaddeaddeaddeaddeaddeaddeaddeaddead00000000000000000000000000000000000000000000000000000000000000000000"
ROUTER_TOKENS_SWAP_CALL_ARGUMENT = [
    ("uint256", "amountIn", 48000000),
    ("uint256", "amountOutMin", 1998523061527233227),
    (
        "(address,address,bool)[]",
        "routes",
        (
            (
                "0xea32a96608495e54156ae48931a7c20f0dcc1a21",
                "0xdeaddeaddeaddeaddeaddeaddeaddeaddead0000",
                False,
            ),
        ),
    ),
    ("address", "to", "0x7c77b132a0cd0ad1c694ab8645affa26c2787d66"),
    ("uint256", "deadline", 1667934767),
]
