import socket
socket = socket.socket()
c_host = input()
c_port = 2101
address_client = (c_host, c_port)
socket.connect(address_client)
print('connected')
socket.send('hello'.encode())
print('data sent')