import socket 
import sys

try: 
    s = socket.socket()
    print ("Socket created successfully")
except socket.error as er:
    print ("socket creation failed with error")

port = 80

s.bind(('',port))
print("socket binded to %s" %(port))

s.listen(5) #is this meaning listen for 5 seconds?
print("socket listening on port %s" %(port))

while True:
    c, addr = s.accept()
    print("Received connection from client")
    c.send('Hello world, thank you for connecting'.encode()) 
    c.close()
    break
