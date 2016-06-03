import mongodb

class Userinfo(object):
    def __init__(self,uid,name,sex,address,intro,artsum,follows,fans,ifmember,ifv,vintro=''):
        self.uid=uid
        self.name=name
        self.sex=sex
        self.address=address
        self.intro=intro
        self.artsum=artsum
        self.follows=follows
        self.fans=fans
        self.ifmember=ifmember
        self.ifv=ifv
        self.vintro=vintro
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

    def save(self):
        mongodb.fzweibouser.insert_one(self.data)

    def find(self):
        return mongodb.fzweibouser.find_one({'uid':self.uid})
