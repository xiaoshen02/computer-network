from socket import *

serverName = 'localhost'
serverPort = 5201

clientSocket = socket(AF_INET, SOCK_DGRAM)
with open("message.txt", "rb") as f:
    message = f.read(2000)
clientSocket.sendto(message, (serverName, serverPort))
modifiedMessage, serverAddress=clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()