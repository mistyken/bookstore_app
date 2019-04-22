import datetime
from mongoengine import Document, StringField, DateTimeField, FloatField


class Book(Document):
    title = StringField(required=True, max_length=200)
    isbn = StringField(required=True, max_length=200)
    author = StringField(required=True, max_length=100)
    price = FloatField(min_value=0)
    published = DateTimeField(default=datetime.datetime.utcnow())
    publisher = StringField(max_length=200)

