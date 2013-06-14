def fulladder(a, b, cin):
  return [a ^ b ^ cin, (a & b) | (cin & (a ^ b))]

A = 11 # => 1011
B =  3 # => 0011

cout = 0
result = 0
for i in range(4):
  sum, cout = fulladder(A & 1, B & 1, cout)
  result |= (sum << i)
  A >>= 1
  B >>= 1

print result, cout
