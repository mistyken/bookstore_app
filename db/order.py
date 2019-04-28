import datetime
from db.book import Book
from mongoengine import Document, StringField, DateTimeField, ReferenceField, ListField, FloatField


class Order(Document):
    customer_name = StringField(required=True, max_length=200)
    books = ListField(ReferenceField(Book, required=True))
    shipping_address = StringField(required=True, max_length=200)
    total_price = FloatField(min_value=0)
    order_date = DateTimeField(default=datetime.datetime.now)

