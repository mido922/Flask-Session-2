from flask import render_template
from app.models import Book


def book_index():
    listOfBooks = Book.get_all_objects()
    return render_template("students/index.html", books=listOfBooks)