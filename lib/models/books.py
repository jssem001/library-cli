#books model lives here
from config import CONN, CURSOR

class Books:
    #register a new book
    @classmethod
    def register_book(cls, book_title, book_author):
        sql = "INSERT INTO books (book_title, book_author) VALUES (?,?)"
        CURSOR.execute(sql, (book_title, book_author))
        CONN.commit()

    #display all books
    @classmethod
    def show_all_books(cls):
        sql = "SELECT * FROM books"
        CURSOR.execute(sql)
        books = CURSOR.fetchall()
        return books