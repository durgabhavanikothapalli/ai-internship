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
CREATE TABLE IF NOT EXISTS weather (
    city VARCHAR(50),
    date DATE,
    max_temp FLOAT,
    min_temp FLOAT
)
""")

url = os.getenv("WEATHER_API_URL")

params = {
    "latitude": 17,
    "longitude": 78,
    "daily": "temperature_2m_max,temperature_2m_min",
    "timezone": "auto"
}

data = requests.get(url, params=params).json()

for i in range(7):
    cursor.execute("""
    INSERT INTO weather VALUES (%s,%s,%s,%s)
    """, (
        "Hyderabad",
        data['daily']['time'][i],
        data['daily']['temperature_2m_max'][i],
        data['daily']['temperature_2m_min'][i]
    ))

conn.commit()

cursor.execute("SELECT * FROM weather")
print(cursor.fetchall())