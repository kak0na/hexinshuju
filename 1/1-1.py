import re
data=['bat','bit','but','hat','hit','hut']
for i in data:
    m=re.match('[bh][aiu]t',i)
    print(m.group())