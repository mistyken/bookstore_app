import datetime
from mongoengine import Document, StringField, DateTimeField


class book(Document):
    title = StringField(required=True, max_length=200)
    isbn = StringField(required=True, max_length=200)
    author = StringField(required=True, max_length=100)
    price = StringField(max_length=10)
    published = DateTimeField(default=datetime.datetime.now)
    publisher = StringField(max_length=200)

