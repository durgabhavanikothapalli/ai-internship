import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer


df = pd.read_csv("dataset.csv")

print("Original Dataset")
print(df.head())

drop_columns = ['PassengerId', 'Name', 'Ticket', 'Cabin']
existing_cols = [col for col in drop_columns if col in df.columns]

df.drop(existing_cols, axis=1, inplace=True)

print("\nColumns after dropping:")
print(df.columns)


num_cols = df.select_dtypes(include=np.number).columns

num_imputer = SimpleImputer(strategy='median')
df[num_cols] = num_imputer.fit_transform(df[num_cols])

cat_cols = df.select_dtypes(include=['object', 'string']).columns

cat_imputer = SimpleImputer(strategy='most_frequent')
df[cat_cols] = cat_imputer.fit_transform(df[cat_cols])

print("\nMissing values handled")

df = pd.get_dummies(df, drop_first=True)

print("\nEncoded Dataset")
print(df.head())


target_column = 'Survived'

X = df.drop(target_column, axis=1)
y = df[target_column]


scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)


X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTrain Test Split Completed")

print("\nX_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)



pd.DataFrame(X_train).to_csv("X_train.csv", index=False)
pd.DataFrame(X_test).to_csv("X_test.csv", index=False)

pd.DataFrame(y_train).to_csv("y_train.csv", index=False)
pd.DataFrame(y_test).to_csv("y_test.csv", index=False)

print("\nAll output files saved successfully")