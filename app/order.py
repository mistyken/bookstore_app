from db.order import Order
from db.inventory import Inventory
import datetime

from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

bp = Blueprint('order', __name__, url_prefix='/order')


@bp.route('/')
def index():
    orders = Order.objects
    return orders.to_json()


@bp.route('/create', methods=['POST'])
def create():
    request_json = request.get_json()
    books = []
    # add only the books that is in stock
    for book in request_json['books']:
        inventory = Inventory.objects(book=book).get()
        if inventory.stock > 0:
            books.append(book)
    order = Order(
        customer_name=request_json['customer_name'],
        books=books,
        shipping_address=request_json['shipping_address'],
        total_price=request_json['total_price'],
        order_status="processing",
        order_date=datetime.datetime.now
    ).save()
    return order.to_json()


@bp.route('/update', methods=['PUT'])
def update():
    request_json = request.get_json()
    if 'id' in request_json and 'order_status' in request_json:
        order = Order.objects(id=request_json['id']).get()
        if request_json['order_status'] == "fulfilled" and order.order_status == "processing":
            for book in order.books:
                inventory = Inventory.objects(book=book).get()
                inventory.stock -= 1
                inventory.save()
            order.order_status = "fulfilled"
            order.save()
        return order.to_json()
