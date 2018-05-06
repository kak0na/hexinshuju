import re
data='1180 Bordeaux Drive'
data='3120 De La Cruz Boulevard'
m=re.match('\d{4}[ a-zA-Z]+',data)
print(m.group())