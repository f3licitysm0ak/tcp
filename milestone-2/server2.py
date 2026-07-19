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


connection, addr = s.accept()
print("Received connection from client")

#receiving message from the client
length_bytes = connection.recv(4)
length = int.from_bytes(length_bytes, byteorder="big")
print(f"Length of the message from client is {length} bytes")
message = connection.recv(length).decode()
print(f"Message received: {message}")

#sending a message back to the client 
message_to_client = "Hello, client!"
message_ba = bytearray(message_to_client, "utf-8")
length_ba = bytearray(len(message_to_client).to_bytes(4, byteorder="big"))
full_ba = length_ba + message_ba
connection.send(full_ba) 

#connection.close()
