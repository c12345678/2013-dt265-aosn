def halfadder(a, b):
  return [a ^ b, a & b]

for pairs in [[0, 0], [0, 1], [1, 0], [1, 1]]:
  s, c = halfadder(*pairs)
  print c, s
