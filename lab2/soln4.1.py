def s2bin(s):
  return [ord(c) for c in s]

def encrypt(M, K):
  if len(M) != len(K):
    raise Exception("Length of plaintext and key must be the same")
  # Convert the plaintext and key to binary representations
  mb = s2bin(M)
  kb = s2bin(K)
  return [mb[i] ^ kb[i] for i in range(len(mb))]

def decrypt(cb, K):
  if len(cb) != len(K):
    raise Exception("Length of ciphertext and key must be the same")
  # Convert the key to binary representation
  kb = s2bin(K)
  mb = [cb[i] ^ kb[i] for i in range(len(cb))]
  return ''.join([chr(c) for c in mb])

C = encrypt("Secret", "aBcDeF")
print decrypt(C, "aBcDeF")        # Sould be "Secret"
