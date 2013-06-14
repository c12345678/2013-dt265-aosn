def bitsfrom(number, start, end):
  if start < 0 or start > 30 or end < 1 or end > 31:
    raise Exception("Indices out of range")

  # Generate a mask with one bits in the region of interest,
  # zeros everwhere else
  mask = 0
  for i in range(start, end):
    mask |= i << 1

  # Maks and shift the bits into place
  return (number & mask) >> start

# Test with some sample inputs
print bin(bitsfrom(170, 1, 2))  # 1010 => 01
