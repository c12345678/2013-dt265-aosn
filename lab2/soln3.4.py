
# Take a list of named variables and a function and generate a full
# truth table
#
# Note that the arity of the passed function must match the number of
# variables passed (in names)

def truthTable(names, F):
  table = []
  #
  # Firstly, generate the combinations of input variables
  #
  ncols = len(names)
  nrows = 2 ** ncols
  for i in range(ncols):
    cols = [names[i]]         # Column heading is variable name
    b = False
    for j in range(nrows):
      if j % (2 ** i) == 0:
        b = not b
      cols.append(b)
    table.append(cols)
  #
  # Secondly, apply the function F() to each row of variables
  #
  result = ['F()']                # Column to hold function result
  for i in range(1, nrows + 1):
    fargs = []                    # Used to build the argument list for F
    for j in range(ncols):
      fargs.append(table[j][i])
    result.append(F(*fargs))      # Using Python's *-operator to expand fargs
  table.append(result)        
  return table

import sys
def prettyPrint(truthTable):
  nrows = len(truthTable)
  ncols = len(truthTable[0])
  for j in range(ncols):
    for i in range(nrows):
      sys.stdout.write(str(truthTable[i][j]))
      sys.stdout.write("\t")
    sys.stdout.write("\n")

F = lambda x, y, z: (not x and y and z) or (not x and y and not z) or (x and z)
table = truthTable(['A', 'B', 'C'], F)
prettyPrint(table)

G = lambda x, y, z: (not x and y) or (x and z)
table = truthTable(['A', 'B', 'C'], G)
prettyPrint(table)
