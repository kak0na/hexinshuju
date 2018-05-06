#创建TCP客户端

from socket import *

HOST='localhost'#'127.0.0.1'
PORT=21567
BUFSIZ=1024
ADDR=(HOST,PORT)
tcpCliSock = socket(AF_INET, SOCK_STREAM)
try:
    HOST=input('HOST:')
    PORT=int(input('PORT:'))
    ADDR=(HOST,PORT)
    tcpCliSock.connect(ADDR)
    print('连接成功')
except:
    print('连接失败，将使用127.0.0.1：21567连接')
    HOST = 'localhost'  # '127.0.0.1'
    PORT = 21567
    BUFSIZ = 1024
    ADDR = (HOST, PORT)
    tcpCliSock.connect(ADDR)

while 1:
    data=input('> ')

    if not data:
        break
    tcpCliSock.send(data.encode())              #将data更改为bytes类型
    data=tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data.decode())                        #将data更改为str类型

tcpCliSock.close()