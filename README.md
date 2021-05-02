# Liquid NFT
Liquid-based Non-Fungible Token based on asset registry and contracts.

## Introduction
An NFT is a Liquid asset with:

- Asset amount = 0.00000001
- Reissue token amount = 0

We will use asset registry contract with some custom fields in order to save a commitment to a NFT contract.

## Asset registry contract
We will add the `ntf` key with `domain` and `hash` fields.

```
{
  "entity": {
    "domain": ""
  },
  "issuer_pubkey": "",
  "name": "",
  "nft": {
    "domain": "",
    "hash": ""
  }
  "precision": 0,
  "ticker": "",
  "version": 0
}
```

The NFT contract will have a special form and will be saved on the domain specified in the `.well-known` folder with name  `nft-hash.json` where hash is the sha256 hash of the same file.

[Contract creation](https://github.com/valerio-vaccaro/Liquid-NFT/blob/main/contract.md) describe how to create the NFT contract.

## Examples
We created a simple python script in order to create NFT contracts and we used in some simple [Examples](https://github.com/valerio-vaccaro/Liquid-NFT/blob/main/examples.md).
