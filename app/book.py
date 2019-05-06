from db.book import Book

from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

bp = Blueprint('book', __name__, url_prefix='/book')


@bp.route('/')
def index():
    if request.args.get('isbn') is not None:
        books = Book.objects(isbn=request.args.get('isbn'))
    elif request.args.get('title') is not None:
        books = Book.objects(title=request.args.get('title'))
    else:
        books = Book.objects.all()
    return books.to_json()
