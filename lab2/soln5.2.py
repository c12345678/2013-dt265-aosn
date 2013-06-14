#
def bin2dec(binaryString):
  decimal = 0
  reversedString = binaryString[::-1]
  for i in range(len(binaryString)):
    c = reversedString[i]
    if c == '1':
      decimal |= (1 << i)
    elif c != '0':
      raise Exception("Invalid binary input: " + binaryString)
  return decimal


# Test with some sample inputs
for b in ['0000', '0101', '1010', '1001', '0110', '1111', '10000', '100000', '10101010']:
  print bin2dec(b)

