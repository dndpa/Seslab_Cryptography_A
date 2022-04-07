import requests
import hashlib
from Crypto.Cipher import AES

r = requests.get('http://aes.cryptohack.org/passwords_as_keys/encrypt_flag/')
result = bytes.fromhex(r.json()['ciphertext'])

with open('words', 'r') as f:
    for words in f:
        words = words.strip()

        kunci = hashlib.md5(words.encode()).digest()
        cipher = AES.new(kunci, AES.MODE_ECB)
        result2 = cipher.decrypt(result)
       
        if result2.startswith('crypto{'.encode()):
            print(result2)
            break