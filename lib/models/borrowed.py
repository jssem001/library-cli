#borrowed books model lives here
from config import CONN, CURSOR
from datetime import datetime, timedelta

class Borrowed:
    #borrow a book
    @classmethod
    def borrow_book(cls, title, author, borrower):
        sql = "SELECT availability FROM books WHERE book_title = ? AND book_author = ?"
        CURSOR.execute(sql, (title, author))
        availability = CURSOR.fetchone()[0]

        if availability == 1:
            sql = "INSERT INTO borrowed (title, author, borrower, return_date) VALUES (?,?,?,?)"
            return_date = datetime.now() + timedelta(weeks=2)
            CURSOR.execute(sql, (title, author, borrower, return_date))
            CONN.commit()

            sql = "UPDATE books SET availability = 0 WHERE book_title = ? AND book_author = ?"
            CURSOR.execute(sql, (title, author))
            CONN.commit()

            print(f"{title} by {author} has been borrowed by {borrower}")
        else:
            print("Book is not available.")    

    
    #return a book
    @classmethod
    def return_book(cls, title, author, borrower):
        sql = "SELECT availability FROM books WHERE book_title = ? AND book_author = ?"
        CURSOR.execute(sql, (title, author))
        availability = CURSOR.fetchone()[0]

        if availability == 0:
            sql = "DELETE FROM borrowed WHERE title = ? AND author = ? AND borrower = ?"
            CURSOR.execute(sql, (title, author, borrower))
            CONN.commit()

            sql = "UPDATE books SET availability = 1 WHERE book_title = ? AND book_author = ?"
            CURSOR.execute(sql, (title, author))
            CONN.commit()

            print(f"{title} by {author} has been returned by {borrower}")
        else:
            print("Book is not borrowed.")
                        

    #display all books
    @classmethod
    def all_borrowed_books(cls):
        sql = "SELECT * FROM borrowed"
        CURSOR.execute(sql)
        books = CURSOR.fetchall()
        return books