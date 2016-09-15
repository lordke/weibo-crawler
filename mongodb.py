from pymongo import MongoClient
#引入pymongo 模块 定义基本数据库配置
MongoClient=MongoClient('localhost',27017)
db=MongoClient.blog   #数据库下的blogcollection
collections=db.articles
weibouser=db.weibouser
fzweibouser=db.fzweibouser
qwweibouser=db.qwweibouser
xj=db.xj