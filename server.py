# server.py 
import socket                                         

# creates an instance of a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# gethostname is a function that gets the host name of the machine
#the program is being run on
host = socket.gethostname()                           

#This is a variable to set the port that you are expected to use
#This will match what is on the client side
port = 8000                                           

# binds the port and host to the socket
serversocket.bind((host, port))                                  

# queue up to 5  connection requests
serversocket.listen(5)                                           

while True:
    # Waits for a client to attemp to connect to our server
    #returns the socket and address of the client
    clientsocket,addr = serversocket.accept()      

    #Prints a message including the information we have on
    # the client
    print("Got a connection from ", addr)

    #Sends a TCP message over to the client
    clientsocket.send(b'Hello Class, did the message get through?')

    recievedData = clientsocket.recv(1024)
    print (recievedData.decode('ascii'))
    recievedData = clientsocket.recv(1024)
    print (recievedData.decode('ascii'))
    #closes the connection with the client socket
    clientsocket.close()
