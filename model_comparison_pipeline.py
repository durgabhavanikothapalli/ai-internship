import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.feature_extraction.text import CountVectorizer


housing = fetch_california_housing()

housing_df = pd.DataFrame(housing.data, columns=housing.feature_names)
housing_df['PRICE'] = housing.target

X_house = housing_df.drop('PRICE', axis=1)
y_house = housing_df['PRICE']

Xh_train, Xh_test, yh_train, yh_test = train_test_split(
    X_house, y_house, test_size=0.2, random_state=42
)

linear_model = LinearRegression()
linear_model.fit(Xh_train, yh_train)

house_predictions = linear_model.predict(Xh_test)

house_mse = mean_squared_error(yh_test, house_predictions)
house_r2 = r2_score(yh_test, house_predictions)


messages = {
    'text': [
        'Congratulations you won a lottery',
        'Please call me later',
        'Win cash now',
        'Meeting scheduled tomorrow',
        'Claim your free gift now',
        'Project submission today',
        'Get free coupons instantly',
        'Lunch at 2 PM'
    ],
    'label': [1, 0, 1, 0, 1, 0, 1, 0]
}

spam_df = pd.DataFrame(messages)

X_spam = spam_df['text']
y_spam = spam_df['label']

vectorizer = CountVectorizer()
X_spam_vectorized = vectorizer.fit_transform(X_spam)

Xs_train, Xs_test, ys_train, ys_test = train_test_split(
    X_spam_vectorized, y_spam, test_size=0.2, random_state=42
)

logistic_model = LogisticRegression()
logistic_model.fit(Xs_train, ys_train)

spam_predictions = logistic_model.predict(Xs_test)

spam_accuracy = accuracy_score(ys_test, spam_predictions)
spam_cm = confusion_matrix(ys_test, spam_predictions)


comparison_df = pd.DataFrame({
    'Model': ['Linear Regression', 'Logistic Regression'],
    'Dataset': ['Housing Prices', 'Spam Emails'],
    'Metric': ['R2 Score', 'Accuracy'],
    'Score': [house_r2, spam_accuracy]
})

print("\nComparison Table:\n")
print(comparison_df)


comparison_df.to_csv('comparison_results.csv', index=False)



plt.figure(figsize=(12, 5))


plt.subplot(1, 2, 1)
plt.scatter(yh_test, house_predictions)
plt.xlabel("Actual")
plt.ylabel("Predicted")
plt.title("Linear Regression")


plt.subplot(1, 2, 2)
plt.imshow(spam_cm)
plt.title("Logistic Regression Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")

plt.tight_layout()
plt.savefig("model_comparison.png")
plt.show()