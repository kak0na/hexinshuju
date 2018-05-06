import re
data='www://www.yahoo.net'
m=re.match('www.+\.(?:com|net|edu)',data)
print(m.group())