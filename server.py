import socket
import time

time.sleep(1)
soc = socket.socket()
host_name = socket.gethostname()
# print(host_name)
ip = socket.gethostbyname(host_name)
# print(ip)
port = 1234
soc.bind((host_name, port))
print(host_name, '({})'.format(ip))
name = input('Enter Name: ')
soc.listen(1)
print('Waiting for incomming connections...')
connection, addr = soc.accept()
print('Received connection from ', addr[0], '(', addr[1], ')\n')
print('Connection Established. Connected From: {}, ({})'.format(addr[0], addr[0]))
# get a connection from client side
client_name = connection.recv(1024)
client_name = client_name.decode()
print(client_name + ' has connected.')
print('Type [bye] to leave the chat room.')
connection.send(name.encode())
while True:
    msg = input('Me > ')
    if msg == '[bye]':
        msg = 'Good Bye...'
        connection.send(msg.encode())
        print('\n')
        break
    connection.send(msg.encode())
    msg = connection.recv(1024)
    msg = msg.decode()
    print(client_name, ' > ', msg)
