# The idea here is to shift all the bits of the input to
# the right, using the least significant bit to build the
# output
def mybin(n):
  binary = []
  while n > 0:
    binary.insert(0, str(n & 1))
    n >>= 1
  # The or clause in the next line deals with n being zero
  return '0b' + (''.join(binary) or '0')

for n in range(16):
  print mybin(n)
