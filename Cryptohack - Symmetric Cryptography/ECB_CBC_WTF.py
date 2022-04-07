import requests

url = 'http://aes.cryptohack.org/ecbcbcwtf'
BLOCK_SIZE = 16

def test():
  response = requests.get(url="%s/encrypt_flag/" % url).json()
  ciphertext = response['ciphertext']
  response = requests.get(url="%s/decrypt/%s" % (url, ciphertext)).json()
  plaintext = bytes.fromhex(response['plaintext'])
  ciphertext = bytes.fromhex(ciphertext)
  result = bytearray()
  
  for i in range((len(ciphertext)//BLOCK_SIZE)-1):
    result.extend(bytearray(a ^ b for a, b in zip(ciphertext[i*BLOCK_SIZE:(i+1)*BLOCK_SIZE], plaintext[(i+1)*BLOCK_SIZE:(i+2)*BLOCK_SIZE])))
  return result.decode()

if __name__ == '__main__':
  result = test()
  print(result)