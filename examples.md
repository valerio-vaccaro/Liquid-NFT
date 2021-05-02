# Generate a valid contract in python
You can use the `liquidNFT.py` for create and decode NFT contract.

## Encoding examples

Create an NFT contract with a reference of a local file.

```
python3 liquidNFT.py encode -n BIBLE -d "Bible NFT" -p "https://l-nft.com/img/bible.jpg"  external -f ./docs/bible.txt
generated nft-77f24c98103f8f661d4cea3c670a4999b79491023c505ce41f7294678fdf79dc.json

cat nft-77f24c98103f8f661d4cea3c670a4999b79491023c505ce41f7294678fdf79dc.json | jq
{
  "content": [
    {
      "hash": "52fe94026565e9b2fa48e0ddf29508b510c9ac7eff43e45f8bfb247e373c9656",
      "type": "text/plain",
      "url": "local:bible.txt"
    }
  ],
  "description": "Bible NFT",
  "name": "BIBLE",

  "picture": "https://l-nft.com/img/bible.jpg",
  "version": 1
}
```

Create an NFT contract with a reference of a remote file.

```
python3 liquidNFT.py encode -n BIBLE -d "Bible NFT" -p "https://l-nft.com/img/bible.jpg" external -u "https://l-nft.com/docs/bible.txt"
generated nft-7f9b66afd4130aca068d2d717f34eb5d6cd2ad8c700297e2ebcd6ca5644f45b1.json

cat nft-7f9b66afd4130aca068d2d717f34eb5d6cd2ad8c700297e2ebcd6ca5644f45b1.json | jq
{
  "content": [
    {
      "hash": "f250d6591bb0017505bb0b9879014ef082bdecaec57eb424acb5b0e9dd7ddcf7",
      "type": "text/plain",
      "url": "https://l-nft.com/docs/bible.txt"
    }
  ],
  "description": "Bible NFT",
  "name": "BIBLE",

  "picture": "https://l-nft.com/img/bible.jpg",
  "version": 1
}
```
(online version use CRLF and not only LF so hash of the file differ)

Create an NFT contract with embedded a local file.

```
python3 liquidNFT.py encode -n BTCWP -d "Bitcoin Whitepaper" -p "https://l-nft.com/img/whitepaper.jpg" embedded -f ./docs/bitcoin.pdf
generated nft-6c34b259ad02b1062966c8ecf9c826e34f3ec7c2ce96a274db0e919554510fd8.json

cat generated nft-6c34b259ad02b1062966c8ecf9c826e34f3ec7c2ce96a274db0e919554510fd8.json | jq
{
  "content": [
    {
      "payload": "..."",
      "type": "application/pdf"
    }
  ],
  "description": "Bitcoin Whitepaper",
  "name": "BTCWP",

  "picture": "https://l-nft.com/img/whitepaper.jpg",
  "version": 1
}
```

Create an NFT contract with embedded a remote file.

```
python3 liquidNFT.py encode -n BTCWP -d "Bitcoin Whitepaper" -p "https://l-nft.com/img/whitepaper.jpg" embedded -u https://l-nft.com/docs/bitcoin.pdf
generated nft-6c34b259ad02b1062966c8ecf9c826e34f3ec7c2ce96a274db0e919554510fd8.json

cat generated nft-6c34b259ad02b1062966c8ecf9c826e34f3ec7c2ce96a274db0e919554510fd8.json | jq
{
  "content": [
    {
      "payload": "..."",
      "type": "application/pdf"
    }
  ],
  "description": "Bitcoin Whitepaper",
  "name": "BTCWP",

  "picture": "https://l-nft.com/img/whitepaper.jpg",
  "version": 1
}
```

Create an NFT contract with an embedded string.

```
python3 liquidNFT.py encode -n STR -d "String based NFT" -p "https://l-nft.com/img/string.jpg" embedded -s "NFT on Liquid -> l-nft.com"
generated nft-869d119ae67eb7f01ccc6c975f62fde3b5dbe515401a049cd02efa463be7abdd.json

cat nft-869d119ae67eb7f01ccc6c975f62fde3b5dbe515401a049cd02efa463be7abdd.json | jq
{
  "content": [
    {
      "payload": "4e4654206f6e204c6971756964202d3e206c2d6e66742e636f6d",
      "type": "text/plain"
    }
  ],
  "description": "String based NFT",

  "name": "STR",
  "picture": "https://l-nft.com/img/string.jpg",
  "version": 1
}
```

## Decoding examples
TBD
