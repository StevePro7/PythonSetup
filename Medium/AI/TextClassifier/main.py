from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

categories = ['rec.autos', 'sci.space']

# 403 Forbidden
data = fetch_20newsgroups(subset='all', categories=categories, remove=('headers','footers','quotes'))

X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)
tfidf = TfidfVectorizer(stop_words='english', max_features=5000)
X_train_tfidf = tfidf.fit_transform(X_train)
X_test_tfidf = tfidf.transform(X_test)

model = LogisticRegression(max_iter=1000)
model.fit(X_train_tfidf, y_train)

y_pred = model.predict(X_test_tfidf)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred, target_names=data.target_names))

sample_texts = [
    "The car engine performance was amazing and smooth.",
    "NASA has announced a new mission to explore Jupiter’s moons.",
    "I don't like the speed of this car"
]

sample_tfidf = tfidf.transform(sample_texts)
preds = model.predict(sample_tfidf)

for text, label in zip(sample_texts, preds):
    print(f"Text: {text}\nPredicted category: {data.target_names[label]}\n")
