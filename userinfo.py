import mongodb

class Userinfo(object):
    def __init__(self,uid,name,sex,address,intro,artsum,follows,fans,ifmember,ifv,vintro=''):
        self.uid=uid  #用户uid
        self.name=name  #用户姓名
        self.sex=sex  #性别
        self.address=address   #地址
        self.intro=intro  # 介绍
        self.artsum=artsum # 总微博数
        self.follows=follows  #关注人数
        self.fans=fans  # 粉丝人数
        self.ifmember=ifmember # 是否微博会员
        self.ifv=ifv # 是否加V
        self.vintro=vintro #  加V认证介绍
        self.data={
            'uid':self.uid ,
            'name':self.name,
            'sex':self.sex,
            'address':self.address,
            'intro' : self.intro,
            'artsum':self.artsum,
            'follows':self.follows ,
            'fans':self.fans,
            'ifmember':self.ifmember,
            'ifv':self.ifv,
            'vintro':self.vintro
        }

    def save(self):   #用户信息操作方法
        mongodb.qwweibouser.insert_one(self.data)

    def find(self):
        return mongodb.qwweibouser.find_one({'uid':self.uid})
