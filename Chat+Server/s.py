import socket
import threading, Queue

from time import gmtime, strftime
import time
import hashlib


HOST = '127.0.0.1'
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

# This is the buffer string
# when input comes in from a client it is added
# into the buffer string to be relayed later
# to different clients that have connected
# Each message in the buffer is separated by a colon :
buffer = " "
connections = []

# custom say hello command
def sayHello():
  print "----> The hello function was called"

#Hashing of the payload
  hash = hashlib.sha224("Nobody inspects the spammish repetition").hexdigest()

print hash

# sample parser function. The job of this function is to take some input
# data and search to see if a command is present in the text. If it finds a
# command it will then need to extract the command.
def parseInput(data, con):
  print str(data)

  # Checking for commands
  if "<time>" in data:
	print strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
	
  if "<Ping>" in data:
	print "Pong"
	
	start_time = time.time()
	print("--- %s seconds ---" % (time.time() - start_time))

# we a new thread is started from an incoming connection
# the manageConnection funnction is used to take the input
# and print it out on the server
# the data that came in from a client is added to the buffer.


def manageConnection(conn, addr):
  global buffer
  print 'Connected by', addr

  conn.send(buffer)
  connections.append(conn)

  while 1:
    data = conn.recv(1024)
    parseInput(data, conn) # Calling the parser, passing the connection
    buffer += " " + str(data) + " "

while 1:
  s.listen(1)
  conn, addr = s.accept()
  # after we have listened and accepted a connection coming in,
  # we will then create a thread for that incoming connection.
  # this will prevent us from blocking the listening process
  # which would prevent further incoming connections
  t = threading.Thread(target=manageConnection, args = (conn,addr))

  t.start()
