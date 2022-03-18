#Soal XOR Properties

import binascii
from pwn import xor

hex_key1 = 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
hex_key21 = '37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'
hex_key23 = 'c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'
hex_flag_key132 = '04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'

byte_key1 = bytes.fromhex(hex_key1)
byte_key21 = bytes.fromhex(hex_key21)
byte_key23 = bytes.fromhex(hex_key23)
byte_flag_key132 = bytes.fromhex(hex_flag_key132)

key1 = byte_key1
key2 = xor(key1, byte_key21)
key3 = xor(key2, byte_key23) 
key123 = xor(byte_key21, key3)

flag = xor(byte_flag_key132, key123)

print(flag)