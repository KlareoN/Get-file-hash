from hashlib import md5, sha1, sha224, sha256, sha384, sha512, shake_128, shake_256, sha3_224, sha3_256, sha3_384, sha3_512
from sys import argv
from os import path
from binascii import crc32
from json import dump


def main():
    if argv[1] is None:
        return print('file is not selected')
    else:
        if path.exists(argv[1]):
            file_open = open(argv[1], 'rb').read()

            hash_table_function = {
                'MD5': md5(file_open).hexdigest(),
                'SHA1': sha1(file_open).hexdigest(),
                'SHA224': sha224(file_open).hexdigest(),
                'SHA256': sha256(file_open).hexdigest(),
                'SHA384': sha384(file_open).hexdigest(),
                'SHA512': sha512(file_open).hexdigest(),
                'SHA3_224': sha3_224(file_open).hexdigest(),
                'SHA3_256': sha3_256(file_open).hexdigest(),
                'SHA3_384': sha3_384(file_open).hexdigest(),
                'SHA3_512': sha3_512(file_open).hexdigest(),
                'SHAKE128': shake_128(file_open).hexdigest(64),
                'SHAKE256': shake_256(file_open).hexdigest(128),
                'CRC32': "%08X" % (crc32(file_open) & 0xFFFFFFFF)
            }
            try:
                if argv[2]:
                    name: str = argv[1].split("\\")[-1]
                    with open(f'hash of file {name}.json', 'w') as f:
                        dump(hash_table_function, f, sort_keys=False, indent=4)
            except:
                for i in hash_table_function:
                    print(f'{i}: {hash_table_function[i]}')
        else:
            return print('not a file in a directory')


if __name__ == '__main__':
    main()