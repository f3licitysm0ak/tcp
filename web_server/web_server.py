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
    connection, addr = s.accept()
    requests = connection.recv(1024).decode()

    for line in requests.splitlines():
        print(f"Line: {line}")
    request = requests.splitlines()[0]
    print(f"Received {request} from client")

    filename = request[5:-9] 

    content = "File not found"    
    with open(filename, "r") as file:
        content = file.read()

            
    connection.send(content.encode())
    connection.close()





