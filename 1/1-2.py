import re
data='sdaf sdf'
m=re.match('[a-zA-Z]+ [a-zA-Z]+',data)
print(m.group())