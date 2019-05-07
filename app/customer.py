from db.customer import Customer

from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

bp = Blueprint('customer', __name__, url_prefix='/customer')


@bp.route('/')
def index():
    customers = Customer.objects
    return customers.to_json()
