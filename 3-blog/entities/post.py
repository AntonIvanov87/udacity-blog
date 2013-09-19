
from google.appengine.ext import db


class Post(db.Model):
    subject = db.StringProperty()
    content = db.StringProperty(multiline=True)
    date = db.DateTimeProperty(auto_now_add=True)
