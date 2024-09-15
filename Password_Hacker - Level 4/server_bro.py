from socket import socket, gethostname, getfqdn, AF_INET, SOCK_STREAM
HOST = gethostname()
print(HOST)
PORT = 12345
print('Process initiated')
while True:
    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        print('Connected')
        # data = s.recv(1000).decode()
        # print(f'received {data}')
        # '''if data == '123456':
        #     s.send('Connection Success'.encode())
        #     break'''