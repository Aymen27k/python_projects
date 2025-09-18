from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column

app = Flask(__name__)
""" db = sqlite3.connect("books-collection.db")
cursor = db.cursor()
#cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit() """
class Base(DeclarativeBase):
  pass
db = SQLAlchemy(model_class=Base)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///book-collection.db"
# initialize the app with the extension
db.init_app(app)

class Books(db.Model):
    id = db.Column(Integer, primary_key=True)
    title = db.Column(String(250), unique=True, nullable=False)
    author = db.Column(String(250), nullable=False)
    rating = db.Column(Float, nullable=False)

with app.app_context():
    db.create_all()



@app.route('/')
def home():
    # Load all books from the database
    result = db.session.execute(db.select(Books).order_by(Books.title))
    all_books = result.scalars().all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        book_name = request.form.get("book_name")
        book_author = request.form.get("book_author")
        book_rating = request.form.get("rating")
        new_book = Books(title=book_name, author=book_author, rating=book_rating)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
        #all_books.append(new_book)
        #print(all_books)
    return render_template("add.html")

@app.route('/edit/<int:book_id>', methods=['GET', 'POST'])
def edit_rating(book_id):
    selected_book = db.get_or_404(Books, book_id)
    if request.method == "POST":
        new_rating = request.form['new_rating']
        selected_book.rating = new_rating
        print(f"new rating = {new_rating}")
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", book=selected_book)

@app.route("/delete_book/<int:book_id>")
def delete_book(book_id):
    book_to_delete = db.get_or_404(Books, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

