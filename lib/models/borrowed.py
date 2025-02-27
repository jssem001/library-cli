#borrowed books model lives here
from config import CONN, CURSOR
from datetime import datetime, timedelta

class Borrowed:
    #borrow a book
    @classmethod
    def borrow_book(cls, title, author, borrower):
        sql = "INSERT INTO borrowed (title, author, borrower, return_date) VALUES (?,?,?,?)"
        return_date = datetime.now() + timedelta(weeks=2)
        CURSOR.execute(sql, (title, author, borrower, return_date))
        CONN.commit()  
    
    #return a book
    @classmethod
    def return_book(cls, title, author, borrower):
        sql = "DELETE FROM borrowed WHERE title = ? AND author = ? AND borrower = ?"
        CURSOR.execute(sql, (title, author, borrower))
        CONN.commit()
                        

    #display all books
    @classmethod
    def all_borrowed_books(cls):
        sql = "SELECT * FROM borrowed"
        CURSOR.execute(sql)
        books = CURSOR.fetchall()
        return books