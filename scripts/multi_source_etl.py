import pandas as pd
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_URL = os.getenv("API_URL")


users = requests.get(f"{API_URL}/users").json()
posts = requests.get(f"{API_URL}/posts").json()

df_users = pd.json_normalize(users)
df_posts = pd.DataFrame(posts)


df_users = df_users[['id', 'name', 'email', 'address.city']]
df_users.rename(columns={'address.city': 'city'}, inplace=True)

df_posts = df_posts[['userId', 'title']]
df_posts.rename(columns={'userId': 'id'}, inplace=True)


df = pd.merge(df_users, df_posts, on='id')


post_count = df_posts.groupby('id').size().reset_index(name='post_count')

df = pd.merge(df_users, post_count, on='id')


df['email'] = df['email'].str.lower()
df['name'] = df['name'].str.strip()
df['city'] = df['city'].str.strip()

df = df.dropna()


df.to_csv('output/merged_data.csv', index=False)

print(df.head())