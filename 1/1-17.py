import re
import os
date={'Mon': 0,'Thu': 0, 'Wed':0,'Tue': 0, 'Fri':0, 'Sat': 0,'Sun': 0 }
os.system('python 1-16.py')
with open('redata.txt','r') as f:
    for data in f.readlines():
        m=re.match('(\w+) ',data).group(1)
        date[m]=date[m]+1
    print(date)