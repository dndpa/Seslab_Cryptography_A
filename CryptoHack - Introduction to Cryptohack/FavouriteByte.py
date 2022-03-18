#Soal Favourite Byte

import binascii
from unittest import result

inihex = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
flag = ''

inibyte = bytearray.fromhex(inihex)

for i in range(256):
    result = []
    for n in inibyte:
        result.append(chr(n^i))
    
    flag = "".join(result)
    if (flag.startswith('crypto')):
        print(flag)
