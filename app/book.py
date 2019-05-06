from db.book import Book

from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

bp = Blueprint('book', __name__, url_prefix='/book')


@bp.route('/')
def index():
    book_isbn = request.args.get('isbn')
    if book_isbn is not None:
        books = Book.objects(isbn=book_isbn)
    else:
        books = Book.objects
    return str([book.to_json() for book in books])
