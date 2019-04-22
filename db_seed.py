from pymongo import MongoClient
import mongoengine


def mongo_db_seed():
    """
    This is a sample mongodb test for populating sample data into mongodb
    :return:
    """
    client = MongoClient('localhost', 27017)
    db = client.bookstore

    books = db.book.find()
    for book in books:
        print(book)

mongo_db_seed()

# if __name__ == "__main__":
#     mongo_db_seed()
