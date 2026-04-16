import pandas as pd
import requests
import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()
API_URL = os.getenv("API_URL")

def extract():
    data = requests.get(f"{API_URL}/posts").json()
    return pd.DataFrame(data)

def transform(df):
    df = df.drop_duplicates()
    df['title_length'] = df['title'].str.len()
    df['body_length'] = df['body'].str.len()
    return df

def load(df):
    df.to_csv('output/final_data.csv', index=False)

    conn = sqlite3.connect('output/data.db')
    df.to_sql('posts', conn, if_exists='replace', index=False)
    conn.close()

def main():
    df = extract()
    df = transform(df)
    load(df)
    print("Pipeline completed successfully")

if __name__ == "__main__":
    main()