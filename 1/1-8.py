import re
data='8941525456465123'
if int(data)<-2147483648 or int(data)>2147483647:
    m=re.match('-?\d+',data).group()
print(m)