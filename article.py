import mongodb  #微博个人信息module
class Article(object):
    def __init__(self,title,author,date,text):
        self.title=title
        self.author=author
        self.date=date
        self.text=text

    def save(self):
        data={'title':self.title,
              'author':self.author,
              'date':self.date,
              'text':self.text}
        mongodb.collections.insert_one(data)
