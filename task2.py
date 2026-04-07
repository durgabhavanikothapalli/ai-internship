import os
import requests
import sqlite3
from dotenv import load_dotenv

load_dotenv()

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
id INTEGER PRIMARY KEY,
name TEXT,
email TEXT,
phone TEXT,
city TEXT,
company TEXT
)
""")

data = requests.get(os.getenv("API_URL")).json()

for user in data:
    cursor.execute("INSERT OR REPLACE INTO users VALUES (?,?,?,?,?,?)", (
        user['id'],
        user['name'],
        user['email'],
        user['phone'],
        user['address']['city'],
        user['company']['name']
    ))

conn.commit()

cursor.execute("SELECT * FROM users")
print(cursor.fetchall())