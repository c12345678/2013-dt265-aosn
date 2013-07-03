import threading

# The ring buffer is a fixed sized list whose size should not exceed
# maxitems. It doesn't matter with you insert into the list, e.g.
# integers, strings, characters, whatever ...
ringbuffer = []
maxitems = 20
readindex = 0
writeindex = 0
mutex = threading.BoundedSemaphore(value = 1)
spaceavail = None # Replace with your semaphore declaration here
itemsavail = None # Replace with your semaphore declaration here
 
# Class to represent a producer thread. Adds a new message to the
# global ring buffer and exits
class Producer(threading.Thread):
  def __init__(self, msg):
    threading.Thread.__init__(self)
    self.msg = msg

  def run(self):
    global ringbuffer, writeindex, mutex, spaceavail, itemsavail, maxitems
    # TODO
    # 1. Wait until a free buffer slot becomes available
    # 2. When one does, write the message into the buffer list, advancing
    #    the write index and accounting for write wrap around
    # 3. Signal that there is one more message to read.
    return

class Consumer(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)

  def run(self):
    global ringbuffer, readindex, mutex, spaceavail, itemsavail, maxitems
    # TODO
    # 1. Wait until a message is available to process
    # 2. When a message becomes available, remove it from the message list,
    #    advancing the read index and handling read index wrapping
    # 3. Print the message contents to the screen
    # 4. Signal that a free message slot is available
    return

# TODO
# Write some test code to create a number of producer and consumer threads
# Verify your bounded buffer implementation above for various numbers of each
#
# Note that you should follow the thread create, start and join pattern in shm2.py
# in order to make this work properly
