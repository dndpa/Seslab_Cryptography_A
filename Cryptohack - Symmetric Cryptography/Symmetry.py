import requests

url = 'http://aes.cryptohack.org/symmetry/'

def encrypted_flag():
    x = requests.get(url + "encrypt_flag/")
    eflag = x.json()['ciphertext']
    return eflag

def encrypt(plain, iv):
    x = requests.get(url + "encrypt/" + plain + "/" + iv + "/")
    result = x.json()['ciphertext']
    return result

ef = encrypted_flag()
iv = ef[:32]
cip = ef[32:]
flag = encrypt(cip, iv)

print(bytes.fromhex(flag))