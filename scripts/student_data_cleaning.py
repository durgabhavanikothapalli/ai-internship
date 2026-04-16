import pandas as pd


df = pd.read_csv('data/messy_students.csv')

print("Before Cleaning:")
print(df.info())
print(df.isnull().sum())


df.columns = df.columns.str.strip().str.lower()


df = df.drop_duplicates()


df['name'] = df['name'].str.strip().str.title()


df['score'] = pd.to_numeric(df['score'], errors='coerce')


df = df[df['score'] >= 0]


df['score'] = df['score'].fillna(df['score'].mean())

def grade(score):
    if score >= 90:
        return 'A'
    elif score >= 75:
        return 'B'
    elif score >= 50:
        return 'C'
    else:
        return 'F'

df['grade'] = df['score'].apply(grade)


df.to_csv('output/clean_students.csv', index=False)

print("After Cleaning:", len(df))