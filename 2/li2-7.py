from socket import *

HOST='localhost'#'127.0.0.1'
PORT=21567
BUFSIZ=1024
ADDR=(HOST,PORT)

updCliSock=socket(AF_INET,SOCK_DGRAM)

while 1:
    data=input('> ')
    if not data:
        break
    updCliSock.sendto(data.encode(),ADDR)
    data,ADDR=updCliSock.recvfrom(BUFSIZ)
    if not data:
        break
    print(data.decode())
updCliSock.close()