def rotr(number, count):
  # Assume 16-bit numbers
  number &= 0xffff;
  count %= 16
  for i in range(count):
    # Save the least significant bit
    lsb = number & 1
    # Shift by one to the right
    number >>= 1
    # Now insert the saved lsb as the msb
    number |= lsb << 15
  return number

def rotl(number, count):
  # Assume 16-bit numbers
  number &= 0xffff;
  count %= 16
  # Rotating left is the same as rotating right by 16 - count
  return rotr(number, 16 - count)

print rotr(1, 1)
print rotl(1, 1)
