# Contract: 0x00000000006c3852cbef3e08e8df289169ede581
SEAPORT_ABI = [
    {
        "inputs": [
            {
                "components": [
                    {
                        "internalType": "address",
                        "name": "considerationToken",
                        "type": "address",
                    },
                    {
                        "internalType": "uint256",
                        "name": "considerationIdentifier",
                        "type": "uint256",
                    },
                    {
                        "internalType": "uint256",
                        "name": "considerationAmount",
                        "type": "uint256",
                    },
                    {
                        "internalType": "address payable",
                        "name": "offerer",
                        "type": "address",
                    },
                    {"internalType": "address", "name": "zone", "type": "address"},
                    {
                        "internalType": "address",
                        "name": "offerToken",
                        "type": "address",
                    },
                    {
                        "internalType": "uint256",
                        "name": "offerIdentifier",
                        "type": "uint256",
                    },
                    {
                        "internalType": "uint256",
                        "name": "offerAmount",
                        "type": "uint256",
                    },
                    {
                        "internalType": "enum BasicOrderType",
                        "name": "basicOrderType",
                        "type": "uint8",
                    },
                    {"internalType": "uint256", "name": "startTime", "type": "uint256"},
                    {"internalType": "uint256", "name": "endTime", "type": "uint256"},
                    {"internalType": "bytes32", "name": "zoneHash", "type": "bytes32"},
                    {"internalType": "uint256", "name": "salt", "type": "uint256"},
                    {
                        "internalType": "bytes32",
                        "name": "offererConduitKey",
                        "type": "bytes32",
                    },
                    {
                        "internalType": "bytes32",
                        "name": "fulfillerConduitKey",
                        "type": "bytes32",
                    },
                    {
                        "internalType": "uint256",
                        "name": "totalOriginalAdditionalRecipients",
                        "type": "uint256",
                    },
                    {
                        "components": [
                            {
                                "internalType": "uint256",
                                "name": "amount",
                                "type": "uint256",
                            },
                            {
                                "internalType": "address payable",
                                "name": "recipient",
                                "type": "address",
                            },
                        ],
                        "internalType": "struct AdditionalRecipient[]",
                        "name": "additionalRecipients",
                        "type": "tuple[]",
                    },
                    {"internalType": "bytes", "name": "signature", "type": "bytes"},
                ],
                "internalType": "struct BasicOrderParameters",
                "name": "parameters",
                "type": "tuple",
            }
        ],
        "name": "fulfillBasicOrder",
        "outputs": [{"internalType": "bool", "name": "fulfilled", "type": "bool"}],
        "stateMutability": "payable",
        "type": "function",
    },
]

# TX: 0xa139231454fd021dd227a94fff6a1b6260890bb95e5f5bf8517af36e228575e6
SEAPORT_FULFILL_ORDER_CALL_INPUT = (
    "0xfb0f3ee1000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000000"
    "0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
    "00000000000000000000000000000000000000000003b53d9d99ecb800000000000000000000000000001850dd8fb9323b01c34"
    "0d0eb1da1ec16cc8ee1a2000000000000000000000000004c00500000ad104d7dbd00e3ae0a5c00560c00000000000000000000"
    "000000bc4ca0eda7647a8ab7c2061c2e118a18a936f13d000000000000000000000000000000000000000000000000000000000"
    "0000561000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000"
    "00000000000000000000000000000002000000000000000000000000000000000000000000000000000000006346e1d20000000"
    "0000000000000000000000000000000000000000000000000636fadcd0000000000000000000000000000000000000000000000"
    "000000000000000000360c6ebe00000000000000000000000000000000000000000589c7ee474bc5850000007b02230091a7ed0"
    "1230072f7006a004d60a8d4e71d599b8104250f00000000007b02230091a7ed01230072f7006a004d60a8d4e71d599b8104250f"
    "0000000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000"
    "0000000000000000000000000024000000000000000000000000000000000000000000000000000000000000002e00000000000"
    "0000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000001"
    "8fae27693b400000000000000000000000000000000a26b00c1f0df003000390027140000faa719000000000000000000000000"
    "00000000000000000000000018fae27693b40000000000000000000000000000a858ddc0445d8131dac4d1de01f834ffcba52ef"
    "10000000000000000000000000000000000000000000000000000000000000041046bd0fda5b934a96ef4700da1b64e03e7451e"
    "6a6ee45a5004b93823ff3baae34b9f1c4f667781b5fedd27dc67339d4fd3e4ae2a873b315090e6312853732f9a1c00000000000"
    "000000000000000000000000000000000000000000000000000360c6ebe"
)
SEAPORT_FULFILL_ORDER_CALL_ARGUMENT = [
    (
        "(address,uint256,uint256,address,address,address,uint256,uint256,uint8,uint256,uint256,bytes32,uint256,bytes32,bytes32,uint256,(uint256,address)[],bytes)",
        "parameters",
        (
            "0x0000000000000000000000000000000000000000",
            0,
            68400000000000000000,
            "0x1850dd8fb9323b01c340d0eb1da1ec16cc8ee1a2",
            "0x004c00500000ad104d7dbd00e3ae0a5c00560c00",
            "0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d",
            1377,
            1,
            2,
            1665589714,
            1668263373,
            b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00",
            24446860302761739304752683030156737591518664810215442929800781758303463785861,
            b"\x00\x00\x00{\x02#\x00\x91\xa7\xed\x01#\x00r\xf7\x00j\x00M`\xa8\xd4\xe7\x1dY\x9b\x81\x04%\x0f\x00\x00",
            b"\x00\x00\x00{\x02#\x00\x91\xa7\xed\x01#\x00r\xf7\x00j\x00M`\xa8\xd4\xe7\x1dY\x9b\x81\x04%\x0f\x00\x00",
            2,
            (
                (1800000000000000000, "0x0000a26b00c1f0df003000390027140000faa719"),
                (1800000000000000000, "0xa858ddc0445d8131dac4d1de01f834ffcba52ef1"),
            ),
            bytes.fromhex(
                "046bd0fda5b934a96ef4700da1b64e03e7451e6a6ee45a5004b93823ff3baae34b9f1c4f667781b5fedd27dc67339d4fd3e4ae2a873b315090e6312853732f9a1c"
            ),
        ),
    )
]
