import pandas as pd
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL")


response = requests.get(f"{API_URL}/posts")
data = response.json()

df = pd.DataFrame(data)


df = df[['userId', 'id', 'title', 'body']]

df['word_count'] = df['title'].str.split().str.len()

df = df[df['word_count'] >= 4]

df['title'] = df['title'].str.title()
df['body'] = df['body'].str.strip()


df.to_csv('output/clean_posts.csv', index=False)

print("Total:", len(data))
print("After Filter:", len(df))