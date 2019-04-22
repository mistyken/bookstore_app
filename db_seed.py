from pymongo import MongoClient
from faker import Faker
from db.book import Book
# from db.customer import Customer
from db.inventory import Inventory
# from db.order import Order
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

    for x in range(3):
        book = Book(
            title=fake.sentence(nb_words=10, variable_nb_words=True, ext_word_list=None),
            isbn=fake.isbn13(separator="-"),
            author=fake.name(),
            price=round(random.uniform(0, 100), 2),
            published=datetime.datetime.utcnow(),
            publisher=fake.company()
        )
        book.save()

    for x in range(3):
        inventory = Inventory(
            book=Book.objects.first().id,
            stock=random.randint(1, 100),
            name=fake.sentence(nb_words=5, variable_nb_words=False, ext_word_list=None),
            location=fake.address()
        )
        inventory.save()

    books = db.book.find()
    for book in books:
        print(book)

    inventories = db.inventory.find()
    for inventory in inventories:
        print(inventory)


mongo_db_seed()

# if __name__ == "__main__":
#     mongo_db_seed()
