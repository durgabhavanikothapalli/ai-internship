import pandas as pd
import numpy as np

data = {
    "study_hours": np.random.randint(1,10,50),
    "sleep_hours": np.random.randint(4,10,50),
    "attendance": np.random.randint(50,100,50)
}

df = pd.DataFrame(data)
df["score"] = df["study_hours"]*10 + np.random.randint(0,10,50)

print(df.corr())

import seaborn as sns
import matplotlib.pyplot as plt

sns.heatmap(df.corr(), annot=True)
plt.show()

sns.regplot(x="study_hours", y="score", data=df)
plt.show()