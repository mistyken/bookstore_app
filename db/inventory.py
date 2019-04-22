from db.book import book
from mongoengine import Document, StringField, ReferenceField, IntField


class inventory(Document):
    book = ReferenceField(book, required=True)
    stock = IntField(required=True, min_value=0)
    name = StringField(max_length=100)
    location = StringField(max_length=200)



