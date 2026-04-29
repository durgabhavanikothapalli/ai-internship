import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

print(df.describe())

sns.histplot(df['total_bill'])
plt.savefig("hist.png")

sns.boxplot(df['total_bill'])
plt.savefig("box.png")

sns.scatterplot(x='total_bill', y='tip', data=df)
plt.savefig("scatter.png")

sns.heatmap(df.corr(), annot=True)
plt.savefig("heatmap.png")

