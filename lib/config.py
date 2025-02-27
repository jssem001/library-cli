import sqlite3
CONN = sqlite3.connect('library.db')
CURSOR = CONN.cursor()

class Database:
    @classmethod
    def create_tables(cls):
        sql_books="""
        CREATE TABLE IF NOT EXISTS books(
        isbn INTEGER PRIMARY KEY,
        book_title varchar(40),
        book_author varchar(40), 
        FOREIGN KEY(book_title) REFERENCES borrowed(title)
        )
        """
        CURSOR.execute(sql_books)
        CONN.commit()

        sql_users="""
        CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY,
        first_name varchar(40),
        last_name varchar(40),
        username varchar(40),
        passcode INTEGER,
        FOREIGN KEY(username) REFERENCES borrowed(borrower)
        )
        """
        CURSOR.execute(sql_users)
        

        sql_borrowed="""
        CREATE TABLE IF NOT EXISTS borrowed(
        title varchar(40),
        author varchar(40),
        borrower varchar(40),
        deadline varchar(40)
        )
        """
        CURSOR.execute(sql_borrowed)
        
        
        CONN.commit()

    @classmethod
#    def drop_tables(cls):
#        sql_books="""
#       DROP TABLE IF EXISTS books
#        """
#       CURSOR.execute(sql_books)
        
#        sql_users="""
#        DROP TABLE IF EXISTS users
#        """
#        CURSOR.execute(sql_users)
        
#        sql_borrowed="""
#        DROP TABLE IF EXISTS borrowed
#        """
#        CURSOR.execute(sql_borrowed)

    def drop_stadiums_table(cls):
        sql = "DROP TABLE IF EXISTS stadiums"
        CURSOR.execute(sql)
        CONN.commit()   
        
        CONN.commit()
