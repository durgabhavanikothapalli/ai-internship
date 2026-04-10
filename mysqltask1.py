import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    author VARCHAR(100),
    year INT,
    genre VARCHAR(50),
    rating FLOAT
)
""")

cursor.executemany("""
INSERT INTO books (title, author, year, genre, rating)
VALUES (%s,%s,%s,%s,%s)
""", [
    ('Book1','Author1',2005,'Fiction',4.5),
    ('Book2','Author2',1999,'Drama',3.8),
    ('Book3','Author3',2010,'Fiction',4.7),
    ('Book4','Author4',2002,'Sci-Fi',4.2)
])

conn.commit()

cursor.execute("SELECT * FROM books")
print(cursor.fetchall())