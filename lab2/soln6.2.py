def fulladder(a, b, cin):
  return [a ^ b ^ cin, (a & b) | (cin & (a ^ b))]

for triples in [[0, 0, 0], [0, 1, 0], [1, 0, 0], [1, 1, 0],
                [0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]]:
  s, c = fulladder(*triples)
  print c, s
