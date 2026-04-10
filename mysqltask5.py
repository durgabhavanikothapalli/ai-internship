import os
import requests
import csv
from dotenv import load_dotenv

load_dotenv()

data = requests.get(os.getenv("API_URL")).json()

with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "name"])

    for user in data:
        writer.writerow([user['id'], user['name']])

print("CSV created successfully")