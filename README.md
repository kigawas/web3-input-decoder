# web3-input-decoder

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/6f10d5104ef4464797ee94b17c7b9371)](https://www.codacy.com/gh/kigawas/web3-input-decoder/dashboard)
[![CI](https://img.shields.io/github/actions/workflow/status/kigawas/web3-input-decoder/ci.yml)](https://github.com/kigawas/web3-input-decoder/actions)
[![Codecov](https://img.shields.io/codecov/c/github/kigawas/web3-input-decoder.svg)](https://codecov.io/gh/kigawas/web3-input-decoder)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/web3-input-decoder.svg)](https://pypi.org/project/web3-input-decoder/)
[![PyPI](https://img.shields.io/pypi/v/web3-input-decoder.svg)](https://pypi.org/project/web3-input-decoder/)
[![License](https://img.shields.io/github/license/kigawas/web3-input-decoder.svg)](https://github.com/kigawas/web3-input-decoder)

A simple offline web3 transaction input decoder for functions and constructors.

## Install

```bash
pip install web3-input-decoder
```

## Quick start

Let's take a [USDT transfer transaction](https://etherscan.io/tx/0x0331fdfa070ee26b1fc7b01b246ef5e58593cbe9f4a02f7f09bf4a2aa640cf35) and the [USDT contract creator transaction](https://etherscan.io/address/0xdac17f958d2ee523a2206206994597c13d831ec7#code) as an example:

```python
>>> import json
>>> import urllib.request
>>> from web3_input_decoder import decode_constructor, decode_function
>>> f = urllib.request.urlopen("https://api.etherscan.io/api?module=contract&action=getabi&address=0xdac17f958d2ee523a2206206994597c13d831ec7")
>>> TETHER_ABI = json.loads(json.load(f)["result"])
>>> decode_function(
        TETHER_ABI, "0xa9059cbb000000000000000000000000f050227be1a7ce587aa83d5013f900dbc3be0611000000000000000000000000000000000000000000000000000000000ecdd350",
    )
[('address', '_to', '0xf050227be1a7ce587aa83d5013f900dbc3be0611'),
 ('uint256', '_value', 248370000)]
>>> decode_constructor(
        TETHER_ABI, "000000000000000000000000000000000000000000000000000000174876e800000000000000000000000000000000000000000000000000000000000000008000000000000000000000000000000000000000000000000000000000000000c00000000000000000000000000000000000000000000000000000000000000006000000000000000000000000000000000000000000000000000000000000000a546574686572205553440000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000045553445400000000000000000000000000000000000000000000000000000000"
    )
[('uint256', '_initialSupply', 100000000000),
 ('string', '_name', 'Tether USD'),
 ('string', '_symbol', 'USDT'),
 ('uint256', '_decimals', 6)]
```

You can also play with it [here](https://replit.com/@kigawas/Web3-input-decoder-quick-start).

### Performance enhancement

If you have lots of inputs in the same contract to decode, consider using [`InputDecoder`](web3_input_decoder/decoder.py#L41).

```python
>>> from web3_input_decoder import InputDecoder
>>> decoder = InputDecoder(TETHER_ABI)
>>> for _ in range(10000):
>>>    decoder.decode_function(
          (
            "0xa9059cbb000000000000000000000000f050227be1a7ce587aa83d5013f900dbc3b"
            "e0611000000000000000000000000000000000000000000000000000000000ecdd350"
          ),
        )
```

## API

- [`decode_constructor`](web3_input_decoder/__init__.py#L12)

  ```python
  def decode_constructor(
      abi: List[dict],
      tx_input: Union[str, bytes],
      bytecode: Optional[Union[str, bytes]] = None,
  ) -> List[Tuple[str, str, Any]]
  ```

  **Parameters**:

  - `abi`: Contract ABI
  - `tx_input`: Transaction input to decode, with or without deployed contract bytecode
  - `bytecode`: Optional deployed contract bytecode. If this is set, `tx_input` should include bytecode

  **Returns**:

  - `List[Tuple[str, str, Any]]`: Decoded type-name-value tuples

- [`decode_function`](web3_input_decoder/__init__.py#L37)

  ```python
  def decode_function(
      abi: List[dict], tx_input: Union[str, bytes]
  ) -> List[Tuple[str, str, Any]]
  ```

  **Parameters**:

  - `abi`: Contract ABI
  - `tx_input`: Transaction input to decode

  **Returns**:

  - `List[Tuple[str, str, Any]]`: Decoded type-name-value tuples

## Rationale

Existing solutions are not satisfying to me, e.g.:

1. [web3py](https://web3py.readthedocs.io/en/latest/web3.contract.html#web3.contract.Contract.decode_function_input) can only decode function calls and it's necessary to be online to set up a provider first.
2. [ethereum-input-decoder](https://github.com/tintinweb/ethereum-input-decoder) is not maintained and it contains several glitches.
