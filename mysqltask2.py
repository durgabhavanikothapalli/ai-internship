import os
import requests
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
CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(50),
    city VARCHAR(50),
    company VARCHAR(100)
)
""")

data = requests.get(os.getenv("API_URL")).json()

for user in data:
    cursor.execute("""
    INSERT INTO users VALUES (%s,%s,%s,%s,%s,%s)
    ON DUPLICATE KEY UPDATE name=VALUES(name)
    """, (
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