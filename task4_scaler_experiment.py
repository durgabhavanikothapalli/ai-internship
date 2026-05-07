import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import (
    StandardScaler,
    MinMaxScaler,
    RobustScaler
)

from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


df = pd.read_csv("dataset.csv")

print("Original Dataset")
print(df.head())


drop_cols = ['PassengerId', 'Name', 'Ticket', 'Cabin']

existing_cols = [col for col in drop_cols if col in df.columns]

df.drop(existing_cols, axis=1, inplace=True)


num_cols = df.select_dtypes(include=np.number).columns

df[num_cols] = df[num_cols].fillna(df[num_cols].median())


cat_cols = df.select_dtypes(include=['object', 'string']).columns

for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode()[0])


df = pd.get_dummies(df, drop_first=True)


target = 'Survived'

X = df.drop(target, axis=1)
y = df[target]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


outliers = X_train.sample(5, random_state=42) * 10

X_train_outlier = pd.concat([X_train, outliers])

y_train_outlier = pd.concat([
    y_train,
    y_train.sample(5, random_state=42)
])


models = {
    "KNN": KNeighborsClassifier(n_neighbors=5),
    "SVM": SVC()
}


scalers = {
    "Raw": None,
    "StandardScaler": StandardScaler(),
    "MinMaxScaler": MinMaxScaler(),
    "RobustScaler": RobustScaler()
}


results = {}


for scaler_name, scaler in scalers.items():

    if scaler:

        X_train_scaled = scaler.fit_transform(X_train_outlier)

        X_test_scaled = scaler.transform(X_test)

    else:

        X_train_scaled = X_train_outlier

        X_test_scaled = X_test

    for model_name, model in models.items():

        model.fit(X_train_scaled, y_train_outlier)

        predictions = model.predict(X_test_scaled)

        accuracy = accuracy_score(y_test, predictions)

        key = f"{model_name}-{scaler_name}"

        results[key] = accuracy


print("\nAccuracy Results\n")

for k, v in results.items():
    print(f"{k}: {round(v, 2)}")



plt.figure(figsize=(12,6))

plt.bar(results.keys(), results.values())

plt.xticks(rotation=45)

plt.ylabel("Accuracy")

plt.xlabel("Model and Scaler")

plt.title("Scaler Sensitivity Experiment")

plt.tight_layout()

plt.show()