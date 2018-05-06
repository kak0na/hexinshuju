import re

with open('redata.txt','r') as f:
    for data in f.readlines():
        data=data.strip()
        m=re.sub('\w+@(\w+)(\.\w+)+','qq@qq.com',data)
        print(m)