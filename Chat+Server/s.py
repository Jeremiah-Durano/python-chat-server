import socket
import threading, Queue
from time import gmtime, strftime
import time
import hashlib
import webbrowser
import ctypes
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

#Hashing of the payload
hash = hashlib.sha224("Nobody inspects the spammish repetition").hexdigest()
print hash


def commands():
    print("--------------------------------------------------------------")
    print("---                          Command List                  ---")
    print("--------------------------------------------------------------")
    print("1: <Commands>   - Displays The List Of Commands               ")
    print("2: <Time>       - Displays Time                               ")
    print("3: <Date>       - Displays Date                               ")
    print("4: <Year>       - Diplays  Year                               ")
    print("5: @Google      - Searches Google                             ")
    print("6: <Ping>       - Simple Ping/Pong return                     ")
    print("7: <    >       -                                             ")
    print("8: <    >       -                                             ")
    print("--------------------------------------------------------------")
    print("---                                                        ---")
    print("--------------------------------------------------------------")

#Google Function
def google(data):
    print "Google function"
    googleStr = data.replace("","")
    googleStr = googleStr.split(':', 1)[-1]
    googleStr = googleStr.strip()
    googleStr = googleStr.replace(" ","+")
    url = "https://www.google.com/"
    webbrowser.open_new_tab(url)

# sample parser function. The job of this function is to take some input
# data and search to see if a command is present in the text. If it finds a
# command it will then need to extract the command.
def parseInput(data, con):
  print str(data)

  # Checking for commands
  if "<Commands>" in data:
    commands()

  if "<Time>" in data:
    print strftime("The Time is: ""%H:%M:%S ", gmtime())

  if "<Year>" in data:
    print strftime("The Year is: ""%Y", gmtime())

  if "<Date>" in data:
    print strftime("The Date is: ""%d %b", gmtime())

  if "<Ping>" in data:
    print "Pong"

    start_time = time.time()
    print("--- %s seconds ---" % (time.time() - start_time))

  if "!Google" in data:
      google(data)
      
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
