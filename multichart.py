import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("iris")

df.hist()
plt.show()

sns.scatterplot(x='sepal_length', y='petal_length', data=df)
plt.show()