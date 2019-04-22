import datetime
from db.customer import customer
from db.book import book
from mongoengine import Document, StringField, DateTimeField, ReferenceField, ListField


class order(Document):
    customer = ReferenceField(customer, required=True)
    books = ListField(ReferenceField(book, required=True))
    shipping_address = StringField(required=True, max_length=200)
    total_price = StringField(max_length=10)
    order_date = DateTimeField(default=datetime.datetime.now)

