from db.book import Book

from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

bp = Blueprint('getbook', __name__, url_prefix='/getbook')



@app.route("/", methods=['GET', 'POST'])
def getBook():
    #request.method and request.form
        #request.method --> going to submit the POST method
        #then it will get request.form
    bookListJson == ""
    if request.method == 'GET':
        if request.form['BookName']:
            bookName = request.form.get('BookName')

            if bookName.isdigit():
                #by ISBN
                print("here")
            else:
                #by name
                books = Book.objects(title=bookName)
                for book in books:
                    bookListJson += str(book.to_json())

            return bookListJson

        else :
            return "validation not successful"


    return render_template('result.html')
