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
capitals = {
"Mexico": "Mexico City",
"Japan": "Tokyo",
"Australia": "Canberra"
}
connection, addr = s.accept()

while True:
    connection.send('Enter a country'.encode())
    country = connection.recv(1024).decode()
    print(f"Received {country} from client")

    if country == "exit":
        break
    if country in capitals.keys():
        capital = capitals[country]
    else:
        capital = "Country not found"
        
    connection.send(f"Capital of {country} is {capital}".encode())

connection.close()



