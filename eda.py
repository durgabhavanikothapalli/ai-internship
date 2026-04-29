import pandas as pd

df = pd.read_csv("marks.csv")

print(df.shape)
print(df.info())
print(df.dtypes)

print(df.isnull().sum())

print(df.describe())

print(df['subject'].value_counts())

df.hist(figsize=(10,8))

import matplotlib.pyplot as plt
plt.show()

df.boxplot()
plt.show()

