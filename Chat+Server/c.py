
# Echo client program
import socket

HOST = '127'    # The remote host
PORT = 20017  # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
#data = s.recv(80000)

print "please enter your username"
name = raw_input()
nameCommand = '<name-' + name + '>'
print "----------------------"



print "The Message log of: " + name + str(data)
while 1:
  text = raw_input()
  s.sendall(name + ": " + "" + text)

# when we send data to the server, we are using a colon
# at the end of a sentence to mark the end of the current sentence
# later when the input comes back, we will then be breaking the input
# into individual parts using the colon : to separate the lines

    
s.close()
