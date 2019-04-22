from pymongo import MongoClient
from faker import Faker
from db.book import Book
from db.customer import Customer
from db.inventory import Inventory
from db.order import Order
import mongoengine
import datetime
import random


def mongo_db_seed():
    """
    This is a sample mongodb test for populating sample data into mongodb
    :return:
    """
    client = MongoClient('localhost', 27017)
    mongoengine.connect('bookstore_db_test', host='localhost', port=27017)
    db = client.bookstore_db_test
    fake = Faker()

    for x in range(10):
        book = Book(
            title=fake.sentence(nb_words=10, variable_nb_words=True, ext_word_list=None),
            isbn=fake.isbn13(separator="-"),
            author=fake.name(),
            price=round(random.uniform(0, 100), 2),
            published=datetime.datetime.utcnow(),
            publisher=fake.company()
        )
        book.save()

    for book in db.book.find():
        inventory = Inventory(
            book=book['_id'],
            stock=random.randint(1, 100),
        )
        inventory.save()

    for x in range(10):
        customer = Customer(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            address=fake.address(),
            email=fake.email(),
            phone=fake.phone_number(),
            customer_since=datetime.datetime.utcnow(),
            orders=[]
        )
        customer.save()

    for customer in db.customer.find():
        for x in range(random.randint(1, 5)):
            books = [book['_id'] for book in db.book.aggregate([{"$sample": {"size": random.randint(1, 3)}}])]
            total = 0.0
            for book in books:
                total = round(total + Book.objects.with_id(book).price)
            order = Order(
                customer_name="{} {}".format(customer['first_name'], customer['last_name']),
                books=books,
                shipping_address=customer['address'],
                total_price=total,
                order_date=datetime.datetime.utcnow()
            )
            order.save()


if __name__ == "__main__":
    mongo_db_seed()
