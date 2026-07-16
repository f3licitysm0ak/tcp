# Import socket module 
import socket             

# Create a socket object 
c = socket.socket()         

# Define the port on which you want to connect 
port = 80               

# connect to the server on local computer 
c.connect(('127.0.0.1', port)) 

# receive data from the server and decoding to get the string.
print ("Server: %s" %(c.recv(1024).decode()))

c.send("Hello server, nice to meet you".encode())



# close the connection 
c.close()