from .book import Book
from mongoengine import Document, ReferenceField, IntField


class Inventory(Document):
    book = ReferenceField(Book, required=True)
    stock = IntField(required=True, min_value=0)



