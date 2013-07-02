# Very basic Posix shell with support for executing a single command
import os
import sys
import shlex
import readline

prompt = "$ "

def parse(cmd):
  # Handy module already exits for splitting command input into tokens
  return shlex.split(cmd)

def execute(argv):
  pid = os.fork()
  if pid == 0:
    # Child process
    for dir in os.getenv('PATH').split(':'):
      try:
        os.execv(dir + '/' + argv[0], argv)
      except OSError:
        # Keep trying each directory in path until we find it
        continue

    # If we get here then execution has failed
    sys.stderr.write('Unrecognised command: ' + argv[0] + '\n')
    os._exit(1)
  else:
    # Parent process waits for child to finish executing
    os.wait()

# Read, print, eval, loop (REPL)
while True:
  try:
    cmd = raw_input(prompt)
    if cmd.strip() == "exit":
      break
    argv = parse(cmd)
    execute(argv)
  except EOFError:
    break
