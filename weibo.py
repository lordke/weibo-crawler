import urllib.request
import http.cookiejar
import gzip
import urllib.parse
import re
from pyquery import PyQuery as pq
import userinfo
import mongodb


m=1
idpattern = re.compile(r'href="/(\d+)/info')
artsumpattern = re.compile(r'>微博\[(\d+)\]<')
followspattern = re.compile(r'>关注\[(\d+)\]<')
fanspattern = re.compile(r'>粉丝\[(\d+)\]<')
addresspattern = re.compile(r'粉丝\d+人&nbsp;(.*?)<')

def ungzip(data):
    try:        # 尝试解压
        print('正在解压.....')
        data = gzip.decompress(data)
        print('解压完毕!')
    except:
        print('未经压缩, 无需解压')
    return data

def getopener():
    proxy=urllib.request.ProxyHandler({'http': 'http://121.69.22.6:8118/'})
    cj = http.cookiejar.CookieJar()
    pro = urllib.request.HTTPCookieProcessor(cj)
    opener = urllib.request.build_opener(pro,proxy)
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36'),
                       ('Origin', 'https://passport.weibo.cn'),('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')]
    return opener

id='15589721246'
password='a123456'
postdata={'username':id,
          'password':password,
          'entry':'mweibo',
          'pagerefer':'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F&wm=3349&vt=4',
          'savestate':'1'
          }
postdata = urllib.parse.urlencode(postdata).encode()
opener = getopener()
data = opener.open('https://passport.weibo.cn/sso/login',postdata)

findurl='http://weibo.cn/find/user?'
def getfinddata(page,school='清华大学'):
    return { 'scho' :school,
             'gender':'0',
             'sschocomp':'1',
             'class' :'school' ,
             'suser':'1',
             'page':page
             }


def getinfo(user,address):
    global m
    try:
        data=opener.open(user,timeout=10).read()
        page=pq(data)
        readdata=data.decode('utf-8')

        uid=idpattern.search(readdata).group(1)
        res = page('.ut .ctt:first').text().split()
        name = res[0]
        sex = res[1].split('/')[0]
        address =address
        intro = page('.ut .ctt:last').text()
        artsum = artsumpattern.search(readdata).group(1)
        follows = followspattern.search(readdata).group(1)
        fans = fanspattern.search(readdata).group(1)
        ifmember = page('.u [alt="M"]').length
        ifv = page('.u [alt="V"]').length
        vintro = ""
        if(ifv):
            vintro=page('.ut .ctt:eq(1)').text()
    except BaseException as e:
        print("***出现错误 无法打开用户介绍界面")
        print(e)
        return

    user=userinfo.Userinfo(uid,name,sex,address,intro,artsum,follows,fans,ifmember,ifv,vintro)
    user.save()
    print('+++成功保存的%s用户信息 总共%s个'% (name,m) )
    m+=1



def getuser(page):

    print('开始了 第%s页' % page)
    i=0
    begin=0

    finddata = urllib.parse.urlencode(getfinddata(page))
    url = findurl + finddata
    try:
        data = opener.open(url,timeout=10)
        data = data.read()
        xy=pq(data)
        data=data.decode('utf-8')
        user=xy('table td:first a:first')

        while(i<user.length):
            n = addresspattern.search(data,begin)
            address = n.group(1)
            begin = n.end()
            name = xy('table td:eq(1) a:first')
            if(mongodb.qwweibouser.find_one({'name':name.eq(i).text()})):
                print("---已保存%s的账号信息" % name.eq(i).text())
                i+= 1
                continue
            userurl='http://weibo.cn'+user.eq(i).attr('href')
            getinfo(userurl,address)
            i+=1
    except BaseException as e:
        print("***出现错误 无法打开搜索界面" )
        print(e)
        return
for y in range(2):
    for x in range(100,401):
        getuser(x+1)
