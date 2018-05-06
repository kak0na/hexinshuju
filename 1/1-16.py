from random import randrange,choice
from string import ascii_lowercase as lc
from sys import maxsize
from time import ctime

tlds = ('com','edu','net','org','gov')
f=open('redata.txt','w')
for i in range(randrange(10,20)):
    dtint = randrange(maxsize)
    dtstr = ctime(dtint)
    llen = randrange(4,8)
    login = ''.join(choice(lc) for j in range(llen))
    dlen = randrange(llen,13)
    dom = ''.join(choice(lc) for j in range(dlen))
    f.write('%s::%s@%s.%s::%d-%d-%d\n'% (dtstr,login,dom,choice(tlds),dtint,llen,dlen))
    #print('%s::%s@%s.%s::%d-%d-%d'% (dtstr,login,dom,choice(tlds),dtint,llen,dlen))
f.close()
