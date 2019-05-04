from db.order import Order

from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

bp = Blueprint('order', __name__, url_prefix='/order')


@bp.route('/')
def index():
    orders = Order.objects
    return str([order.to_json() for order in orders])
