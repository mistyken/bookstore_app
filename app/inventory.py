from db.inventory import Inventory

from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

bp = Blueprint('inventory', __name__, url_prefix='/inventory')


@bp.route('/')
def index():
    inventories = Inventory.objects
    return str([inventory.to_json() for inventory in inventories])
