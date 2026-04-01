import requests
import csv
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("POSTS_API")

response = requests.get(url)

if response.status_code == 200:
    posts = response.json()
    
    # Save posts.csv
    with open("posts.csv", "w", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["id", "title", "body"])
        
        for post in posts:
            writer.writerow([post["id"], post["title"], post["body"]])

# Read and filter
filtered_posts = []

with open("posts.csv", "r", encoding='utf-8') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        if len(row["title"].split()) > 5:
            print(row["title"])
            filtered_posts.append(row)

# Save filtered_posts.csv
with open("filtered_posts.csv", "w", newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
    writer.writeheader()
    writer.writerows(filtered_posts)