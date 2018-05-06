import re
data='-1123.2'
m=re.match('-?\d+\.?\d+',data).group()
print(m)