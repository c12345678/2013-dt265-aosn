# Very basic Posix shell with support for executing a single command
import os
import sys
import shlex
import readline

prompt = "$ "

def parse(cmd):
  # Handy module already exits for splitting command input into tokens
  return shlex.split(cmd)

def execute(cmd, argv):
  try:
    os.execv(cmd, argv)
  except OSError:
    return

def call(argv):
  pid = os.fork()
  if pid == 0:
    # Child process
    if '/' in cmd:
      # Relative or absolute path specified
      execute(argv[0], argv)
    else:
      for dir in os.getenv('PATH').split(':'):
        # Keep trying each directory in PATH until we find it
        execute(dir + '/' + argv[0], argv)

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
    if cmd.strip() == "":
      continue
    if cmd.strip() == "exit":
      break
    argv = parse(cmd)
    call(argv)
  except EOFError:
    break
