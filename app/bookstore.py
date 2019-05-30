from db.book import Book
from db.order import Order
from db.inventory import Inventory
from db.customer import Customer
from app.auth import login_required
import datetime

from flask import (
    Blueprint, flash, redirect, render_template, request, url_for, g, session
)

bp = Blueprint('bookstore', __name__)

shopping_cart = []


@bp.route('/')
def index():
    available_book_list = get_book_list()

    return render_template('bookstore/index.html', books=available_book_list)


@bp.route('/addcart', methods=['POST'])
@login_required
def add_to_cart():
    copies = request.form.get('copies')
    book_id = request.form.get('book_id')
    order = create_order(g.user['id'], int(copies), book_id)

    return render_template('bookstore/cart.html', books=order.books, total=order.total_price)


@bp.route('/checkoutoption', methods=['POST'])
def at_checkout():
    if request.form['submit_btn'] == 'Keep Browsing':
        return redirect(url_for('bookstore.index'))
    elif request.form['submit_btn'] == 'Checkout':
        order = Order.objects(id=session.get("order_id")).first()

        if len(order.books) < 1:
            flash("You can't check out with empty cart")
            return redirect(url_for('bookstore.index'))
        else:
            return purchase_books()
    elif request.form['submit_btn'] == 'Clear Cart':
        order = Order.objects(id=session.get("order_id")).first()
        order.delete()
        session['order_id'] = None
        flash("Shopping cart cleared")
        return redirect(url_for('bookstore.index'))


def get_book_list():
    available_books = []
    books = Book.objects.all()
    for book in books:
        inventory = Inventory.objects(book=book).get()
        if inventory.stock > 0:
            cur_book = {'book': book, 'inventory': inventory.stock}
            available_books.append(cur_book)
    return available_books


def create_order(user_id, copies, book_id):
    book = Book.objects(id=book_id).first()
    customer = Customer.objects(id=user_id).first()
    books = []
    total = 0.0
    while copies > 0:
        books.append(book)
        total = round(total + Book.objects.with_id(book_id).price, 2)
        copies -= 1

    """checking to see if there's a order id already stored in session"""
    if session.get("order_id"):
        order = Order.objects(id=session.get("order_id")).first()
        order.total_price = round(order.total_price + total, 2)
        for book in books:
            order.books.append(book)
        order.save()
    else:
        order = Order(
                customer_name="{} {}".format(customer.first_name, customer.last_name),
                books=books,
                shipping_address=customer.address,
                total_price=total,
                order_status="processing",
                order_date=datetime.datetime.now
            ).save()
        session["order_id"] = str(order.id)

    return order


@bp.route('/order_complete')
@login_required
def purchase_books():
    customer = Customer.objects(id=session.get("user_id")).first()
    if session['order_id']:
        order = Order.objects(id=session.get("order_id")).first()
        if len(order.books) < 1:
            flash("Please add some book to cart first")
            return redirect(url_for('bookstore.index'))
    else:
        flash("Please add some book to cart first")
        return redirect(url_for('bookstore.index'))
    customer.orders.append(order)
    customer.save()
    flash("Order complete. The order ID is {}".format(order.id))
    session['order_id'] = None
    return redirect(url_for('bookstore.index'))
