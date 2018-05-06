import re
data=['fdaf fdasf','fdas,fda','fdaf      fdasf']
for i in data:
    m=re.match('[a-zA-Z]+[,\s]+[a-zA-Z]+',i)
    print(m.group())