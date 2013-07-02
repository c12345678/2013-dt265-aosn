import os
import shutil
import subprocess

# 7.1 What is the "name" of your running OS?
print os.name

# 7.2 What is your user name? [echo $USER]
print os.getlogin()

# 7.3 What is your current directory? [pwd]
print os.getcwd()

# 7.4 What is your python process id? [echo $$]
print os.getpid()

# 7.5 What is the value of the PATH environment variable? [echo $PATH]
print os.getenv('PATH')

# 7.5 Make a directory called "testdir"
os.mkdir('testdir')

# 7.6 Change into the directory you have just made
os.chdir('testdir')

# 7.7 Create a file in this new directory and add some text to it
f = open('testfile', 'w')
f.write('this is some file text...')
f.close()

# 7.8 Open the file a display its contents
with open('testfile', 'r') as f:
  data = f.read()
  print data

# 7.9 Then remove the directory and all of the files in it
os.chdir('..')
shutil.rmtree('testdir')

# 7.10 Execute the "ls -l" command from Python
subprocess.call(["ls", "-l"])
