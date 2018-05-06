import re
datas=['800-555-1212','555-1212']
for data in datas:
    m=re.match('(\d{3}-)?\d{3}-\d{4}',data).group()
    print(m)