import json
import requests
import hashlib
import magic
import argparse
import binascii

parser = argparse.ArgumentParser(description='Create a contract for Liquid NFT')

subparsers = parser.add_subparsers(dest='command')
subparsers.required = True

action_parser = subparsers.add_parser('encode')
action_parser.add_argument('-n', '--name', help='NFT name', required=True)
action_parser.add_argument('-d', '--description', help='NFT description', required=True)
action_parser.add_argument('-p', '--picture', help='NFT picture', required=True)

encodesubparsers = action_parser.add_subparsers(dest='type')
encodesubparsers.required = True

external_action_parser = encodesubparsers.add_parser('external')
external_action_parser.add_argument('-f', '--file', type=argparse.FileType('rb'), help=f'File to include')
external_action_parser.add_argument('-u', '--url', help=f'Url to include')

embedded_action_parser = encodesubparsers.add_parser('embedded')
embedded_action_parser.add_argument('-f', '--file', type=argparse.FileType('rb'), help=f'File to include')
embedded_action_parser.add_argument('-u', '--url', help=f'Url to include')
embedded_action_parser.add_argument('-s', '--string', help=f'String to include (ascii)')

decode_action_parser = subparsers.add_parser('decode')
decode_action_parser.add_argument('-f', '--file', type=argparse.FileType('r'), help=f'Contract to decode')

args = parser.parse_args()

if args.command == 'encode':

    contract_obj = {
      'name':args.name,
      'description':args.description,
      'picture': args.picture,
      'version': 1,
      'content':[],
    }

    if args.type == 'embedded':
        if args.string is not None:
            print('String')
            mimetype = 'text/plain'
            payload = args.string.encode("utf-8").hex()
        elif args.url is not None:
            url = args.url
            # Download content
            filename = args.url.split('/')[-1]
            r = requests.get(url, allow_redirects=True)
            open(filename, 'wb').write(r.content)
            # get mimetype
            mime = magic.Magic(mime=True)
            mimetype = mime.from_file(filename)
            payload = r.content.hex()
        elif args.file is not None:
           filename = args.file.name.split('/')[-1]
           url = 'local:'+filename
           # get mimetype
           mime = magic.Magic(mime=True)
           mimetype = mime.from_file(args.file.name)
           # get payload
           bytes = args.file.read()
           payload = bytes.hex()
        else:
           print('argument not in ["string", "url", "file"] set!')
           exit(1)
        contract_obj['content'] = [{
            'type': mimetype,
            'payload':payload,
        }]

    elif args.type == 'external':
        if args.url is not None:
            url = args.url
            # Download content
            filename = args.url.split('/')[-1]
            r = requests.get(url, allow_redirects=True)
            open(filename, 'wb').write(r.content)
            # get mimetype
            mime = magic.Magic(mime=True)
            mimetype = mime.from_file(filename)
            # calculate hash
            filehash = hashlib.sha256(r.content).hexdigest()
        elif args.file is not None:
            filename = args.file.name.split('/')[-1]
            url = 'local:'+filename
            # get mimetype
            mime = magic.Magic(mime=True)
            mimetype = mime.from_file(args.file.name)
            # calculate hash
            bytes = args.file.read() # read entire file as bytes
            filehash = hashlib.sha256(bytes).hexdigest();
        else:
            print('argument not in ["url", "file"] set!')
            exit(1)
        contract_obj['content'] = [{
             'type': mimetype,
             'url': url,
             'hash': filehash,
         }]

    else:
        print('argument not in ["embedded", "external"] set!')
        exit(1)

    # serialize the contract and calculate the hash
    contract = json.dumps(contract_obj, separators=(',',':'), sort_keys=True)

    sha256_c = hashlib.sha256()
    sha256_c.update(contract.encode('ascii'))
    contract_hash = sha256_c.hexdigest()

    # save the contract
    generated_filename = 'nft-'+contract_hash+'.json'
    print('generated '+generated_filename)
    f = open(generated_filename, 'w')
    f.write(contract)
    f.close()

elif args.command == 'decode':
    contract = args.file.read()
    filename_hash = args.file.name.split('-')[1][:-5]
    # check hash
    filehash = hashlib.sha256(contract.encode()).hexdigest()
    if filename_hash != filehash:
        print('Invalid contract - hash mismatch!')
    contract = json.loads(contract)
    print('Name: '+contract['name'])
    print('Description: '+contract['description'])
    print('Picture: '+contract['picture'])
    for c in contract['content']:
        if 'payload' in c: # Embedded content
            payload = binascii.unhexlify(c['payload'])
            # save payload
            f = open('payload.bin', 'wb')
            f.write(payload)
            f.close()
        elif 'url'in contract['content']:
            print('Url: '+c['url'])
            print('Hash: '+c['hash'])

        if url[:6] == 'local:': # local url -> check if file is present
            print('local')
            print('TBD')

        else: # remote url -> download
            print('remote')
            print('TBD')

        #r = requests.get(url, allow_redirects=True)
        #open(filename, 'wb').write(r.content)
        # check hash

    else:
        print('Unknown content')
