from db.book import Book

from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

bp = Blueprint('bookstore', __name__)


@bp.route('/')
def index():
    books = Book.objects.all()
    return render_template('bookstore/index.html', books=books)

