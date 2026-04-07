import os
import requests
import sqlite3
from dotenv import load_dotenv

load_dotenv()

conn = sqlite3.connect("weather.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS weather (
city TEXT,
date TEXT,
max_temp REAL,
min_temp REAL
)
""")

url = os.getenv("WEATHER_API_URL") + "?latitude=17&longitude=78&daily=temperature_2m_max,temperature_2m_min&timezone=auto"
data = requests.get(url).json()

for i in range(7):
    cursor.execute("INSERT INTO weather VALUES (?,?,?,?)", (
        "Hyderabad",
        data['daily']['time'][i],
        data['daily']['temperature_2m_max'][i],
        data['daily']['temperature_2m_min'][i]
    ))

conn.commit()

cursor.execute("SELECT * FROM weather")
print(cursor.fetchall())