import re
data='www.gmail.edu'
m=re.match('www.[a-zA-Z]+(?:\.com)*(\.cn|\.org|\.net|\.edu)+',data).group()
print(m)