import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder


df = pd.read_csv("dataset.csv")

print("Original Dataset")
print(df.head())


df['pickup'] = pd.to_datetime(df['pickup'])
df['dropoff'] = pd.to_datetime(df['dropoff'])


df['day_of_week'] = df['pickup'].dt.dayofweek


df['hour'] = df['pickup'].dt.hour


df['is_weekend'] = df['day_of_week'] >= 5


df['trip_duration'] = (
    df['dropoff'] - df['pickup']
).dt.total_seconds() / 60


df['fare_per_mile'] = (
    df['fare'] / (df['distance'] + 1)
)


df['tip_per_mile'] = (
    df['tip'] / (df['distance'] + 1)
)


df['log_distance'] = np.log1p(df['distance'])


df['fare_category'] = pd.cut(
    df['fare'],
    bins=[0,10,30,100],
    labels=['low','medium','high']
)



num_cols = df.select_dtypes(include=np.number).columns

df[num_cols] = df[num_cols].fillna(df[num_cols].median())


cat_cols = df.select_dtypes(include=['object', 'string']).columns

for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode()[0])


le = LabelEncoder()

df['payment'] = le.fit_transform(df['payment'])

target = 'payment'

df.drop(['pickup', 'dropoff'], axis=1, inplace=True)

df = pd.get_dummies(df, drop_first=True)


X = df.drop(target, axis=1)
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


model = RandomForestClassifier(random_state=42)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)


print("\nFeature Engineering Completed Successfully")

print("\nEngineered Features:")
print([
    'day_of_week',
    'hour',
    'is_weekend',
    'trip_duration',
    'fare_per_mile',
    'tip_per_mile',
    'log_distance',
    'fare_category'
])

print("\nModel Accuracy:", round(accuracy, 2))

print("\nDataset Shape:", df.shape)