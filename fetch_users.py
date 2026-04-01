import requests
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("USERS_API")

response = requests.get(url)

if response.status_code == 200:
    users = response.json()
    
    for user in users:
        print("Name:", user["name"])
        print("Email:", user["email"])
        print("City:", user["address"]["city"])
        print("-" * 20)
else:
    print("Failed to fetch users")