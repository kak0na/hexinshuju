import re
data="2154-1524-1524-6358"
m=re.findall("\d{4}-\d{6}-\d{5}|\d{4}-\d{4}-\d{4}-\d{4}",data)
print(m)