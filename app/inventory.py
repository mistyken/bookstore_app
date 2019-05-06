from db.inventory import Inventory
import json
import bson

from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

bp = Blueprint('inventory', __name__, url_prefix='/inventory')


@bp.route('/')
def index():
    inventory = Inventory.objects

    inventory_dict = json.loads(inventory.to_json())

    for inv_dict, inv in zip(inventory_dict, inventory):
        inv_dict['book'] = inv.book.to_mongo()

    return bson.json_util.dumps(inventory_dict)
