import requests

x = requests.get('http://aes.cryptohack.org/block_cipher_starter/encrypt_flag/')
result = x.json()['ciphertext']
endpointdec = 'http://aes.cryptohack.org/block_cipher_starter/decrypt/' + result
dec = requests.get(endpointdec)
nextresult = dec.json()['plaintext']

by = bytes.fromhex(nextresult)
final_result = by.decode()
print(final_result)