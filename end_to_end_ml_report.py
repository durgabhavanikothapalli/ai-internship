import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


housing = fetch_california_housing()

housing_df = pd.DataFrame(housing.data, columns=housing.feature_names)
housing_df['PRICE'] = housing.target

print("\nDataset Information:\n")
print(housing_df.info())


print("\nMissing Values:\n")
print(housing_df.isnull().sum())

print("\nStatistical Summary:\n")
print(housing_df.describe())

housing_df.hist(figsize=(12, 10))
plt.savefig("feature_distribution.png")
plt.show()


correlation = housing_df.corr()

plt.figure(figsize=(10, 8))
plt.imshow(correlation)
plt.colorbar()
plt.title("Correlation Heatmap")
plt.savefig("correlation_heatmap.png")
plt.show()


X = housing_df.drop('PRICE', axis=1)
y = housing_df['PRICE']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)


mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:\n")
print("Mean Squared Error:", mse)
print("R2 Score:", r2)


plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")
plt.title("Actual vs Predicted")
plt.savefig("model_evaluation.png")
plt.show()


report = f'''
END-TO-END MACHINE LEARNING REPORT

Dataset Used:
California Housing Dataset

Model Used:
Linear Regression

Evaluation Metrics:
Mean Squared Error: {mse}
R2 Score: {r2}

Observations:
1. The model performs reasonably well.
2. Features show moderate correlations.
3. Scaling improved model stability.
'''

with open('findings_report.txt', 'w') as file:
    file.write(report)

print("\nReport generated successfully.")