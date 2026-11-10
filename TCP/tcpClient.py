from socket import *
serverName='localhost'
serverPort=5201
clientSocket=socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence=input('Input lowercase sentence: ')
clientSocket.send(sentence.encode())
modifiledSentence=clientSocket.recv(1024).decode()
print('From Server: ',modifiledSentence)
clientSocket.close()