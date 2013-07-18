#!/usr/bin/env python

#
# This example code is taken from the following source:
#   http://pymotw.com/2/select/
#

import select
import socket
import sys
import Queue

# Do not block forever (milliseconds)
TIMEOUT = 5000
# Our server host name and port
HOST = '127.0.0.1'
PORT = 10000

# Create a non-blocking TCP/IP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)

# Bind the socket to the port
server_address = (HOST, PORT)
print >>sys.stderr, 'starting up on %s port %s' % server_address
server.bind(server_address)

# Listen for incoming connections
server.listen(5)

# Keep up with the queues of outgoing messages
message_queues = {}

# Commonly used flag sets (constants are defined in the select libary)
READ_ONLY = select.POLLIN | select.POLLPRI | select.POLLHUP | select.POLLERR
READ_WRITE = READ_ONLY | select.POLLOUT

# Set up the poller
poller = select.poll()
poller.register(server, READ_ONLY)

# Map file descriptors to socket objects (initialising with our server)
fd_to_socket = { server.fileno(): server }

while True:

    # Wait for at least one of the sockets to be ready for processing
    print >>sys.stderr, '\nwaiting for the next event'
    events = poller.poll(TIMEOUT)

    for fd, flag in events:

        # Retrieve the actual socket from its file descriptor
        s = fd_to_socket[fd]

        # Handle inputs
        if flag & (select.POLLIN | select.POLLPRI):

            if s is server:
                # When the main server socket is readable, that really means
                # there is a pending connection from a client. The new
                # connection is registered with the READ_ONLY flags to watch
                # for new data to come through it.

                # A "readable" server socket is ready to accept a connection
                connection, client_address = s.accept()
                print >>sys.stderr, 'new connection from', client_address
                connection.setblocking(0)
                fd_to_socket[ connection.fileno() ] = connection
                poller.register(connection, READ_ONLY)

                # Give the connection a queue for data we want to send
                message_queues[connection] = Queue.Queue()

            else:
                # Sockets other than the server are existing clients,
                # and recv() is used to access the data waiting to be read.
                # If recv() returns any data, it is placed into the
                # outgoing queue for the socket and the flags for that
                # socket are changed using modify() so poll() will watch
                # for the socket to be ready to receive data.
                data = s.recv(1024)

                if data:
                    # A readable client socket has data
                    print >>sys.stderr, 'received "%s" from %s' % (data, s.getpeername())
                    message_queues[s].put(data)
                    # Add output channel for response
                    poller.modify(s, READ_WRITE)

                    # An empty string returned by recv() means the client disconnected,
                    # so unregister() is used to tell the poll object to ignore the socket.

                else:
                    # Interpret empty result as closed connection
                    print >>sys.stderr, 'closing', client_address, 'after reading no data'
                    # Stop listening for input on the connection
                    poller.unregister(s)
                    s.close()

                    # Remove message queue
                    del message_queues[s]

                    # The POLLHUP flag indicates a client that hung up the connection without
                    # closing it cleanly. The server stops polling clients that disappear.

        elif flag & select.POLLHUP:
            # Client hung up
            print >>sys.stderr, 'closing', client_address, 'after receiving HUP'
            # Stop listening for input on the connection
            poller.unregister(s)
            s.close()

        elif flag & select.POLLOUT:
            # In the handling of writable sockets, modify() is used to change the flags for
            # the socket in the poller

            # Socket is ready to send data, if there is any to send.
            try:
                next_msg = message_queues[s].get_nowait()
            except Queue.Empty:
                # No messages waiting so stop checking for writability.
                print >>sys.stderr, 'output queue for', s.getpeername(), 'is empty'
                poller.modify(s, READ_ONLY)
            else:
                print >>sys.stderr, 'sending "%s" to %s' % (next_msg, s.getpeername())
                s.send(next_msg)

                # And finally, any events with POLLERR cause the server to close the socket.

        elif flag & select.POLLERR:
            print >>sys.stderr, 'handling exceptional condition for', s.getpeername()
            # Stop listening for input on the connection
            poller.unregister(s)
            s.close()

            # Remove message queue
            del message_queues[s]
