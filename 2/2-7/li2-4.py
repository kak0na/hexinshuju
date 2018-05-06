#创建TCP客户端
import re
from socket import *

HOST='localhost'#'127.0.0.1'
PORT=21567
BUFSIZ=1024
ADDR=(HOST,PORT)
tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)
data=''
while 1:
    data=input('客户端：')
    if not data:
        break
    tcpCliSock.send(data.encode())       #将data更改为bytes类型
    data=tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    data=data.decode()
    print('服务器：',data)                        #将data更改为str类型
tcpCliSock.close()