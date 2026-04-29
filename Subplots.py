import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("iris")

fig, axes = plt.subplots(2,2)

sns.histplot(df['sepal_length'], ax=axes[0,0])
sns.boxplot(y=df['sepal_length'], ax=axes[0,1])
sns.scatterplot(x='sepal_length', y='petal_length', data=df, ax=axes[1,0])
sns.countplot(x='species', data=df, ax=axes[1,1])

plt.tight_layout()
plt.show()