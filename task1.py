import sqlite3

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT,
author TEXT,
year INTEGER,
genre TEXT,
rating REAL
)
""")

cursor.executemany("""
INSERT INTO books (title, author, year, genre, rating)
VALUES (?,?,?,?,?)
""", [
('Book1','Author1',2005,'Fiction',4.5),
('Book2','Author2',1999,'Drama',3.8),
('Book3','Author3',2010,'Fiction',4.7),
('Book4','Author4',2002,'Sci-Fi',4.2),
('Book5','Author5',2015,'Fiction',4.9),
('Book6','Author6',1995,'Drama',3.5),
('Book7','Author7',2020,'Sci-Fi',4.8),
('Book8','Author8',2008,'Fiction',4.1)
])

conn.commit()

cursor.execute("SELECT * FROM books")
print(cursor.fetchall())