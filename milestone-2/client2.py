import socket             

c = socket.socket()         

# Define the port on which you want to connect 
port = 80               

# connect to the server on local computer 
c.connect(('127.0.0.1', port)) 

#sending initial message to the server
message = "Hello, server!"
message_ba = bytearray(message, "utf-8")
length_ba = bytearray(len(message).to_bytes(4, byteorder="big"))
full_ba = length_ba + message_ba
c.send(full_ba) 

#receiving response from the server
length_bytes = c.recv(4)
length = int.from_bytes(length_bytes, byteorder="big")
print(f"Length of the message from server is {length} bytes")
message_from_server = c.recv(length).decode()
print(f"Message received: {message_from_server}")

# close the connection 
#c.close()