from db.book import Book
from db.inventory import Inventory
from db.customer import Customer

from flask import (
    Blueprint, flash, redirect, render_template, request, url_for, g
)

bp = Blueprint('bookstore', __name__)

shopping_cart = []


@bp.route('/')
def index():

    available_book_list = get_book_list()

    return render_template('bookstore/index.html', books=available_book_list)


@bp.route('/addcart', methods=['POST'])
def add_to_cart():
    copies = request.form.get('copies')
    # create_order(copies, isbn)

    return render_template('bookstore/order.html')


@bp.route('/checkoutoption', methods=['POST'])
def at_checkout():
    if request.method == 'POST':

        if request.form['submit_btn'] == 'Keep Browsing':
            return redirect(url_for('bookstore.index'))
        elif request.form['submit_btn'] == 'Checkout':
            return redirect(url_for('order.create'))


def get_book_list():
    available_books = []
    books = Book.objects.all()
    for cur_book in books:
        inventory = Inventory.objects(book=cur_book).get()
        if inventory.stock > 0:
            available_books.append(cur_book)
    return available_books


def create_order(copies, isbn):
    book = Book.objects(isbn=isbn).get()
    customer = Customer.objects(first_name="Kennth").get()


# def purchase_books():
