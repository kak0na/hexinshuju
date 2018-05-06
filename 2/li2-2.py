#创建TCP服务器
#-*- coding=utf-8 -*-
from socket import *
from time import ctime,timezone
import os

HOST= ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)
while  1:
    try:
        print('waiting for connection...')
        tcpCliSock,addr = tcpSerSock.accept()
        print('...connected from:',addr)
        while 1:
            data=tcpCliSock.recv(BUFSIZ)
            if not data:
                break
            data=data.decode()     #将data更改为str类型
            data={'data':data}
            data['系统名称']=os.name
            data['文件列表']=os.listdir()
            data['时间']=ctime()
            tcpCliSock.send(('%s'%data).encode()) #将 [%s] %s 更改为bytes类型

    except:
        pass
    finally:
        tcpCliSock.close()
tcpSerSock.close()