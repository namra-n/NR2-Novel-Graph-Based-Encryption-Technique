def rc4(key):

  S = list(range(100))
  j = 0
  for i in range(100):
    j = (j + S[i] + key[i % len(key)]) % 100
    S[i], S[j] = S[j], S[i]

  i = j = 0
  while True:
    i = (i + 1) % 100
    j = (j + S[i]) % 100
    S[i], S[j] = S[j], S[i]
    yield S[(S[i] + S[j]) % 100]

def generate_rc4_sequence(seed, length):

  key = bytes(seed)
  cipher = rc4(key)
  return [next(cipher) for _ in range(length)]
