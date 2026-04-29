import requests
import pandas as pd

cities = ["Delhi","Mumbai","Chennai","Hyderabad","Bangalore"]

data = []

for city in cities:
    url = f"https://api.open-meteo.com/v1/forecast?latitude=28&longitude=77&daily=temperature_2m_max&timezone=auto"
    res = requests.get(url).json()
    
    for temp in res['daily']['temperature_2m_max']:
        data.append([city, temp])

df = pd.DataFrame(data, columns=["city","max_temp"])

print(df.describe())

import seaborn as sns
import matplotlib.pyplot as plt

sns.histplot(df['max_temp'])
plt.show()

sns.boxplot(x='city', y='max_temp', data=df)
plt.show()