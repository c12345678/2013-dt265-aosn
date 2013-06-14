# Implementation of the builtin hex() function using modulo aritmetic
def myhex(n):
  hexDigits = "0123456789ABCDEF"
  quotient = n
  results = []
  while quotient != 0:
     remainder = quotient % 16       # Modulo operator
     results.insert(0, hexDigits[remainder])
     quotient = quotient / 16
  return '0x' + (''.join(results) or '0')

# Test it with various inputs
for n in [0, 1, 2, 3, 15, 16, 255, 1023, 1024]:
  print myhex(n)
