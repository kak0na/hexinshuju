import re

with open('redata.txt','r') as f:
    for data in f.readlines():
        data=data.strip()
        m=re.match('(.+?)::',data).group(1)
        print(m)