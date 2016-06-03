import  article
import urllib.request
import urllib.parse
import http.cookiejar
from pyquery import PyQuery as pq

def downarticle(aurl):
    i=0
    data = urllib.request.urlopen(aurl).read().decode()
    page = pq(data)
    title=page('.article-details h1:first').text()
    author=page('.f1.author').text()
    date=page('.f1.time').text()
    p=page('.details.lph-article-comView>p')
    text=''
    while(i<p.length):
        text=text+'<p>'+p.eq(i).html()+'</p>'
        i+=1
    art=article.Article(title,author,date,text)
    art.save()



def geteach(url):
    data=urllib.request.urlopen(url).read().decode()
    page=pq(data)
    articleurl=page('.body-list a ')
    i=0
    while i<articleurl.length:
        aurl=articleurl.eq(i).attr('href')
        downarticle(aurl)
        i+=2

geteach('http://m.leiphone.com/')
