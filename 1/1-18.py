import re
import os
date={'Mon': 0,'Thu': 0, 'Wed':0,'Tue': 0, 'Fri':0, 'Sat': 0,'Sun': 0 }
os.system('python 1-16.py')
with open('redata.txt','r') as f:
    for data in f.readlines():
        data=data.strip()
        m=re.match('(.+?)::',data).group(1)
        n=re.search('::(\d+)',data).group(1)
        print(m,':',n)