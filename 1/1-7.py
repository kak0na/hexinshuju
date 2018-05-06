import re
data='123'
if int(data)>=-2147483648 and int(data)<=2147483647:
    m=re.match('-?\d+',data).group()
print(m)