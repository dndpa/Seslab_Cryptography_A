import requests

url = 'http://aes.cryptohack.org/triple_des/'
key_hex = '0101010101010101FEFEFEFEFEFEFEFE'

a = requests.get(url + 'encrypt_flag/' + key_hex).json()['ciphertext']
b = requests.get(url + 'encrypt/' + key_hex + '/' + a).json()['ciphertext']
print(bytes.fromhex(b))