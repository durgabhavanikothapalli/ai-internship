import pandas as pd
import matplotlib.pyplot as plt

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


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


df = pd.DataFrame(messages)

print("\nDataset:\n")
print(df)


X = df['text']
y = df['label']


vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)


X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized, y, test_size=0.2, random_state=42
)


model = LogisticRegression()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)


accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

print("\nAccuracy:", accuracy)
print("\nConfusion Matrix:\n", cm)
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))


plt.figure(figsize=(5, 5))
plt.imshow(cm)
plt.title("Confusion Matrix")
plt.colorbar()
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.savefig("spam_confusion_matrix.png")
plt.show()