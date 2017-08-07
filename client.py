# client.py  
import socket

# create a socket object
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = ""                          

port = 8000

# connection to hostname on the port.
mysocket.connect((host, port))                               

# Receive no more than 1024 bytes
recievedData = mysocket.recv(1024)
print (recievedData.decode('ascii'))

mysocket.send(b'Testing?')

request =input("What's the directory of the text file you want?")
mysocket.send(request.encode(encoding='ascii'))

with open(request.split("/")[-1:][0], 'wb') as file:
    while True:
        print("receiving data..")
        data = mysocket.recv(1024)
        
        if not data:
            break
        file.write(data)


mysocket.close()
