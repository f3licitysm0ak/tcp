import socket 
import sys
from datetime import datetime
from dateutil import tz

try: 
    s = socket.socket()
except socket.error as er:
    print ("socket creation failed with error")

port = 80

s.bind(('',port))

s.listen(5) #is this meaning listen for 5 seconds?
print("socket listening on port %s" %(port))


connection, addr = s.accept()
print("Received connection from client")

#FUNCTION DEFS START
#receiving message from the client
def receive_message(connection):
    length_bytes = connection.recv(4)
    length = int.from_bytes(length_bytes, byteorder="big")
    message = connection.recv(length).decode()
    print(f"Client: {message}")
    return message

#sending a message back to the client 
def send_message(connection, message_to_client):
    message_ba = bytearray(message_to_client, "utf-8")
    length_ba = bytearray(len(message_to_client).to_bytes(4, byteorder="big"))
    full_ba = length_ba + message_ba
    connection.send(full_ba)

def upper(message):
    uppercase_msg = message.upper()
    return uppercase_msg

def reverse(message):
    return message[::-1]

def get_time(target_timezone):
    local_tz = tz.tzlocal()
    target_tz = tz.gettz(target_timezone)
    local_time = datetime.now(local_tz)
    converted_time = local_time.astimezone(target_tz)
    return converted_time

#FUNCTION DEFS END

full_command = receive_message(connection)
chunks = full_command.split(maxsplit=1)
cmd = chunks[0]
msg = chunks[1]

msg_to_client = ""
match cmd:
    case "ECHO":
        msg_to_client = msg.strip()
    case "UPPER":
        msg_to_client = upper(msg)
    case "REVERSE":
        msg_to_client = reverse(msg)
    case "TIME":
        raw_time = get_time(msg)
        msg_to_client = raw_time.strftime("%Y-%m-%d %H:%M:%S")
    case _:
        msg_to_client = "Unknown command, supported commands are ECHO, UPPER, REVERSE, and TIME."

send_message(connection, msg_to_client)   


connection.close()
