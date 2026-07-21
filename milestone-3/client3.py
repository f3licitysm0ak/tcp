import socket   
import sys          

c = socket.socket()         

# Define the port on which you want to connect 
port = 80               

# connect to the server on local computer 
c.connect(('127.0.0.1', port)) 

#FUNCTION DEFS START
#sending initial message to the server
def send_message(connection, message_to_server):
    message_ba = bytearray(message_to_server, "utf-8")
    length_ba = bytearray(len(message_to_server).to_bytes(4, byteorder="big"))
    full_ba = length_ba + message_ba
    connection.send(full_ba)

#receiving response from the server
def receive_message(connection):
    length_bytes = connection.recv(4)
    length = int.from_bytes(length_bytes, byteorder="big")
    message_from_server = connection.recv(length).decode()
    print(f"Server: {message_from_server}")
    return message_from_server
#FUNCTION DEFS END

msg_to_send = "ECHO Hello, World!"
if len(sys.argv) > 1:
    msg_to_send = sys.argv[1] + " " + sys.argv[2]

send_message(c, msg_to_send)

receive_message(c)


# close the connection 
#c.close()