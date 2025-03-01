import sqlite3

# Connect to database (or create if it doesn't exist)
CONN = sqlite3.connect("library.db")
CURSOR = CONN.cursor()

# Create tables
CURSOR.execute("""
CREATE TABLE IF NOT EXISTS books (
    isbn INTEGER PRIMARY KEY,
    book_title VARCHAR(40),
    book_author VARCHAR(40),
    availability INTEGER DEFAULT 1
)
""")

CURSOR.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(40),
    last_name VARCHAR(40),
    username VARCHAR(40),
    passcode INTEGER
)
""")

CURSOR.execute("""
CREATE TABLE IF NOT EXISTS borrowed (
    title VARCHAR(40),
    author VARCHAR(40),
    borrower VARCHAR(40),
    return_date DATE
)
""")

# Insert sample data
CURSOR.executemany("INSERT INTO books (isbn, book_title, book_author, availability) VALUES (?, ?, ?, ?)", [
    (1, "dreamers", "andrew endere", 0),
    (2, "chasers", "jojo clarke", 0),
    (3, "Cold Kitchen", "Caroline Eden", 1),
    (4, "Love and Need", "Adam Plunkett", 1),
    (5, "Code Noir", "Canisia Lubrin", 1),
    (6, "Lorne", "Susan Morrison", 1),
    (7, "Helen of Troy", "Maria Zoccola", 1),
    (8, "After Lives", "Megan Marshall", 1),
    (9, "The Dissenters", "Youssef Rakha", 1),
    (10, "Black in Blues", "Imani Perry", 1),
    (11, "Make Your Own Job", "Erik Baker", 1),
    (12, "Open Socrates", "Agnes Callard", 1),
    (13, "Before Elvis", "Preston Lauterbach", 1),
    (14, "Going Home", "Tom Lamont", 1),
    (15, "Mood Machine", "Liz Pelly", 1)
])

CURSOR.executemany("INSERT INTO users (first_name, last_name, username, passcode) VALUES (?, ?, ?, ?)", [
    ("Joshua", "Sese", "sesery", 654321),
    ("Samiya", "Watkins", "sammyW", 112233)
])

CURSOR.executemany("INSERT INTO borrowed (title, author, borrower, return_date) VALUES (?, ?, ?, ?)", [
    ("chasers", "jojo clarke", "sese18", "2025-03-14 11:21:23.844369"),
    ("dreamers", "andrew endere", "sammyW", "2025-03-14 12:48:43.179562")
])

# Commit and close
CONN.commit()
CONN.close()
print("Database seeded successfully!")
