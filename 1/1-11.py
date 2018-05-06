import re
data='zhangsan-001@gmail.com.cn '
m=re.match('[\w-]+@[a-zA-Z]+(?:\.com|\.cn)+',data).group()
print(m)