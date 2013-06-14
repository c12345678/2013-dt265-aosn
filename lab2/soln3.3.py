# Take a list of named variables and generate truth table
# independent variables
def truthTable(names):
  table = []
  nvars = len(names)
  nrows = 2 ** nvars
  for i in range(nvars):
    cols = [names[i]]       # Column heading is variable name
    b = False
    for j in range(nrows):
      if j % (2 ** i) == 0:
        b = not b
      cols.append(b)
    table.append(cols)
  return table

import sys
def prettyPrint(truthTable):
  rows = len(truthTable)
  cols = len(truthTable[0])
  for j in range(cols):
    for i in range(rows):
      sys.stdout.write(str(truthTable[i][j]))
      sys.stdout.write("\t")
    sys.stdout.write("\n")

table = truthTable(['A', 'B', 'C'])
prettyPrint(table)
