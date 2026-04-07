import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
score INTEGER,
grade TEXT
)
""")

cursor.executemany("INSERT INTO students (name, score) VALUES (?,?)", [
("A", 90), ("B", 40), ("C", 70)
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