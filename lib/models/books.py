#books model lives here
from config import CONN, CURSOR

class Books:
    #register a new book
    @classmethod
    def register_book(cls, book_title, book_author):
        # sql = "ALTER TABLE books ADD COLUMN availability INTEGER DEFAULT 1"
        # CURSOR.execute(sql)
        # CONN.commit()

        # sql = "UPDATE books SET availability = 1"
        # CURSOR.execute(sql)
        # CONN.commit()
        
        sql = "INSERT INTO books (book_title, book_author, availability) VALUES (?,?, 1)"
        CURSOR.execute(sql, (book_title, book_author))
        CONN.commit()

    #display all books
    @classmethod
    def show_all_books(cls):
        sql = "SELECT * FROM books"
        CURSOR.execute(sql)
        books = CURSOR.fetchall()
        return books