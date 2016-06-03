import re
import urllib.request
import os
from pyquery import PyQuery as pq
from lxml import etree
import mongodb

a=r'href="/(\d+)/info'
print(a)
idpattern = re.compile(a)

f=open('F:/Documents/3.html','r', encoding='utf-8',errors='ignore')
data=f.read()
page=pq(data)
user=page('table td:eq(1) a:first')
for i in range(5):
    print(useruser.eq(i).text())
m=5



a=re.search(r'href="/(\d+)/info',r'<a href="/1663983930/info">资料</a>')
artsumpattern = re.compile(r'>微博\[(\d+)\]<')
followspattern = re.compile(r'>关注\[(\d+)\]<')
fanspattern = re.compile(r'>粉丝\[(\d+)\]<')
addresspattern = re.compile(r'粉丝\d+人&nbsp;(.*?)<')
'''

data=urllib.request.urlopen('http://www.maeda-atsuko.cn/index.php')
#print(data.read().decode('gbk'))
print(type(data))
a=data.read()
print(len(a))
print(len(a.decode('gbk')))

print(type(data))
💕-97年水瓶座的敏蜀黍康猴猴🙉🎀爱画画的蜀黍➕V：piaocanmin...
print('成功保存%s个用户信息'% m )



x=page('table td:eq(1)').text()
x = x.split()



n=addresspattern.search(data)
x=n.group(1)
print(x)

begin=n.end()
print(begin)

n=addresspattern.search(data,begin)

x=n.group(1)
print(x)

begin=n.end()
print(begin)

n=addresspattern.search(data,begin)
x=n.group(1)
print(x)

artsum=artsumpattern.search(data).group(1)

follows=followspattern.search(data).group(1)
fans=fanspattern.search(data).group(1)
print(artsum,follows,fans)
uid=idpattern.search(data).group(1)
print(uid)
y=page('.ut .ctt:eq(1)').text()
print(y)
x=page('.u [alt="V"]')
print(x)

print(a.groups())
print(a.group(0))
print(a.group(1))
'''