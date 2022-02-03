import socket

cs = socket.socket()

cs.connect(('localhost',9999))

cname = input('Enter your name: ')

while True:
    msg_rcv = cs.recv(1024).decode()
    
    print(msg_rcv)

    msg = input(f'{cname}: ')
    
    cs.send(bytes(f'{cname}: {msg}','utf-8'))
    
    if(msg=='bye' or msg == 'Bye'):
        break
    
cs.close()