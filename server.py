import socket

ss = socket.socket()    #server_socket

print('Socket created...')

ss.bind(('localhost',9999))

ss.listen(1)

print('Waiting for connections...')

sname = input('Enter your name: ')

cs, addr = ss.accept() #client_socket
    
print('Connected with ',addr)
    
cs.send(bytes(f'{sname}: welcome','utf-8'))

while True:
    '''cs, addr = ss.accept() #client_socket
    
    print('Connected with ',addr)
    
    cs.send(bytes(f'{sname}: welcome','utf-8'))'''
    
    msg_rec = cs.recv(1024).decode()
    
    print(msg_rec)
    
    
    msg = input(f'{sname}: ')
    
    cs.send(bytes(f'{sname}: {msg}','utf-8'))
    
    if(msg=='bye' or msg == 'Bye'):
        break
    
cs.close()