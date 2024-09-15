import socket

server = socket.socket()
serverHost = socket.gethostname()
print(serverHost)
serverPort = 2101
serverAddress = (serverHost, serverPort)
server.bind(serverAddress)
server.listen()
print('Waiting for any incoming connections...')
print(serverHost)
while True:
    clientHost, clientPort = server.accept()
    print(f'{clientPort} has connected to the server!!')
    response = server.recv(1024)
    print(response.decode())
