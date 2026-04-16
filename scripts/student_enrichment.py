import pandas as pd

df = pd.read_csv('output/clean_students.csv')


def grade(score):
    if score >= 90:
        return 'A'
    elif score >= 75:
        return 'B'
    elif score >= 60:
        return 'C'
    elif score >= 50:
        return 'D'
    else:
        return 'F'

df['grade'] = df['score'].apply(grade)

df['passed'] = df['score'] >= 50


def category(score):
    if score >= 80:
        return 'High'
    elif score >= 50:
        return 'Medium'
    else:
        return 'Low'

df['category'] = df['score'].apply(category)


df['rank'] = df['score'].rank(ascending=False)


summary = df.groupby('grade')['score'].agg(['count', 'mean', 'min', 'max'])

print(summary)


df = df.sort_values(by='rank')

df.to_csv('output/enriched_students.csv', index=False)

print(df.head())