import re
data="<type 'int'>"
m=re.search("<type '([a-z_]+)'>",data).group(1)
print(m)