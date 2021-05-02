## NFT contract
The NFT contract is a JSON document able to connect some external document or information to a token issuance transaction.

```
{
  "name": "",
  "description": "",
  "picture": "",
  "version": 1,
  "content": [
    {
      ...
    }
  ]

}
```

Content contain an array (usually has only 1 element) of elements connected with the NFT.

This file i saved in `.well-known/` folder with name `nft-<hash>.json` where `<hash>` is the sha256 hash of the file.

Elements in the content array can be external or embedded.

### External elements
A content element can point to an external file, an hash is added at creation time.

```
{
  "type": "",
  "url": "",
  "hash": ""
}
```

### Embedded elements
A content element can be an embedded string of hexadecimal characters, this is useful for embedded content inside NFT contract.

```
{
  "type": "",
  "payload": ""
}
```
