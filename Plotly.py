import plotly.express as px
import seaborn as sns

df = sns.load_dataset("iris")

fig = px.scatter(df, x="sepal_length", y="petal_length", color="species")

fig.show(renderer="browser")