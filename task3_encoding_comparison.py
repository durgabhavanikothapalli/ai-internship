import pandas as pd
import time

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


df = pd.read_csv("dataset.csv")


df = df.ffill()
target = 'Survived'


label_df = df.copy()

le = LabelEncoder()

for col in label_df.select_dtypes(include='object').columns:
    label_df[col] = le.fit_transform(label_df[col])

X = label_df.drop(target, axis=1)
y = label_df[target]

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

start = time.time()

model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

pred = model.predict(X_test)

end = time.time()

print("\nLabel Encoding Accuracy:")
print(accuracy_score(y_test, pred))

print("Training Time:", end-start)

print("Feature Count:", X.shape[1])


ohe_df = pd.get_dummies(df, drop_first=True)

X = ohe_df.drop(target, axis=1)
y = ohe_df[target]

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

start = time.time()

model.fit(X_train, y_train)

pred = model.predict(X_test)

end = time.time()

print("\nOne Hot Encoding Accuracy:")
print(accuracy_score(y_test, pred))

print("Training Time:", end-start)

print("Feature Count:", X.shape[1])