import pytest
from db.db_seed import mongo_db_seed
from db.book import Book
from db.customer import Customer
from db.inventory import Inventory
from db.order import Order


@pytest.fixture(scope="module")
def init_db():
    test_db_name = "bookstore_db_test_1"
    db = mongo_db_seed(test_db_name)
    yield db
    print("teardown {}".format(test_db_name))
    db.drop_database(test_db_name)


def test_entry_counts(init_db):
    book_count = Book.objects.count()
    assert book_count == 10
    inventory_count = Inventory.objects.count()
    assert inventory_count == 10
    customer_count = Customer.objects.count()
    assert customer_count == 10
    order_count = Order.objects.count()
    assert order_count >= 10

