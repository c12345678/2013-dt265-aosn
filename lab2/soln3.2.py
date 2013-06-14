# Function takes 3 Boolean variables
# Note the use of parentheses to force the right evaluation order

def F(X, Y, Z):
  return (X and Y and not Z) or (not X and Y and not Z) or (X and Z)

# Call function F() for all combinations of X, Y, Z
for X in [True, False]:
  for Y in [True, False]:
    for Z in [True, False]:
      print X, "\t", Y, "\t", Z, "\t", F(X, Y, Z)
