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
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    score INT,
    grade VARCHAR(2)
)
""")

cursor.executemany("""
INSERT INTO students (name, score)
VALUES (%s,%s)
""", [
    ("A", 90),
    ("B", 40),
    ("C", 70)
])

cursor.execute("""
UPDATE students SET grade =
CASE
    WHEN score >= 90 THEN 'A'
    WHEN score >= 60 THEN 'B'
    ELSE 'F'
END
""")

cursor.execute("DELETE FROM students WHERE score < 50")

conn.commit()

cursor.execute("SELECT * FROM students")
print(cursor.fetchall())