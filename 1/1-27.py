import re

with open('redata.txt','r') as f:
    for data in f.readlines():
        data=data.strip()
        m=re.match('(.+?) (.+?) (.+?) (.+?) (.+?)::',data).groups()
        print(m[-1],'年',m[1],'月',m[2],'日')