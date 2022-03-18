#Soal Base64

import base64
import binascii

hexstring = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'
toBase64 = base64.b64encode(bytes.fromhex(hexstring))
print(toBase64)