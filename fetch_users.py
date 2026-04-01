import requests
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("USERS_API")

response = requests.get(url)

if response.status_code == 200:
    users = response.json()

    for user in users:
        print(user["name"], "|", user["email"], "|", user["address"]["city"])
else:
    print("Error fetching users")