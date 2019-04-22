from .book import Book
from mongoengine import Document, StringField, ReferenceField, IntField


class Inventory(Document):
    book = ReferenceField(Book, required=True)
    stock = IntField(required=True, min_value=0)
    name = StringField(max_length=100)
    location = StringField(max_length=200)



