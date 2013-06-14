# De Morgan's Laws

def law1(a, b):
  return not(a and b) == (not a or not b)

def law2(a, b):
  return not(a or b) == (not a and not b)

# We want to see a clean sweep of True values here...
for a in [True, False]:
  for b in [True, False]:
    print law1(a, b), law2(a, b)
