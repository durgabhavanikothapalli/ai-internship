import matplotlib.pyplot as plt
import seaborn as sns


df = sns.load_dataset("iris")


plt.plot(df['sepal_length'])

plt.title("Sepal Length Trend")
plt.xlabel("Index")
plt.ylabel("Sepal Length")

plt.show()