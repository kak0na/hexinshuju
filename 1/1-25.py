import re

with open('redata.txt','r') as f:
    for data in f.readlines():
        data=data.strip()
        m=re.search('::(\w+)@(.*?)::',data).groups()
        print(m)