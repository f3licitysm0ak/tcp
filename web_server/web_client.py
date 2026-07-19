# Import socket module 
import socket             

# Create a socket object 
c = socket.socket()         

# Define the port on which you want to connect 
port = 80               

# connect to the server on local computer 
c.connect(('127.0.0.1', port)) 

request = input("Enter request: ")
c.send(request.encode())

print(c.recv(1024).decode())

c.close()

