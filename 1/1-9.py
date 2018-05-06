import re
data='123.2'
m=re.match('-?\d+\.\d+',data).group()
print(m)