from pymongo import MongoClient
MongoClient=MongoClient('localhost',27017)
db=MongoClient.blog
collections=db.articles
weibouser=db.weibouser
fzweibouser=db.fzweibouser