import socket

s = socket.socket()
s_host = socket.gethostname()
s_port = 2101
address_server = (s_host, s_port)
s.bind(address_server)
s.listen(4)
print('Waiting for any incoming connections...')
print(s_host)
c_host, c_port = s.accept()
print(f'{c_port} has connected to the server!!')
# while True:
# data = s.recv(1024)
# print('data received')
# print((data.decode()))