import time, socket, sys

print('Client Serer...')
time.sleep(1)

soc = socket.socket()
shost = socket.gethostname()
ip = socket.gethostbyname(shost)

print(shost, '({})'.format(ip))
server_host = input('Enter server\'s IP Address: ')
name = input('Enter Name: ')
port = 1234
print('Trying to connect to the server: {}, ({})'.format(server_host, port))
time.sleep(1)

soc.connect((server_host, port))
print('Connected.\n')

soc.send(name.encode())
server_name = soc.recv(1024)
server_name = server_name.decode()
print('{} has joined... '.format(server_name))
print('Enter [bye] to exit.')
while True:
    msg = soc.recv(1024)
    msg = msg.decode()
    print(server_name, ' > ', msg)
    msg = input('Me > ')
    if msg == '[bye]':
        msg = 'Leaving th chat room...'
        soc.send(msg.encode())
        print('\n')
        break
    soc.send(msg.encode())
