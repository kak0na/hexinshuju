import requests
import re





url="https://www.amazon.cn/gp/bestsellers/books/ref=sv_b_3"
try:
    headers={
        'Host':'www.amazon.cn',
        'Referer':'https://www.amazon.cn/gp/new-releases/books/ref=sv_b_2',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    }
    r=requests.get(url,headers=headers)
    r.raise_for_status()
    r.encoding='utf-8'
    text=r.text
    data=re.findall('(?!>)<img alt="(.*?)"',text)
    i=0
    for data in data:
        i+=1
        if i>20 :break
        print(i,':',data)
except:
    print('获取失败')