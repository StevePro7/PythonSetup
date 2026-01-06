# Step 1: Download the Dataset in Colab
import kagglehub

# Download dataset
#path = kagglehub.dataset_download("algord/fake-news")
path = "/home/stevepro/.cache/kagglehub/datasets/algord/fake-news/versions/1"
print("Dataset path:", path)

# Step 2: Load the CSV File
import pandas as pd
import os

df = pd.read_csv(os.path.join(path, "FakeNewsNet.csv"))
#print(df.head())

# # Step 3: Understand the Dataset (DO NOT SKIP THIS)
#print(df.info())

# Data columns (total 5 columns):
#  #   Column         Non-Null Count  Dtype
# ---  ------         --------------  -----
#  0   title          23196 non-null  object
#  1   news_url       22866 non-null  object
#  2   source_domain  22866 non-null  object
#  3   tweet_num      23196 non-null  int64
#  4   real           23196 non-null  int64

#print(df.isnull().sum())

real=df["real"].value_counts()
print(real)
# 1    17441
# 0     5755

# Step 4: Feature Selection
df = df[["title", "real"]]
df.columns = ["text", "label"]

# Step 5: Text Cleaning (Machines Hate Noise)
import re
import string


import re
import string

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\s+', ' ', text).strip()
    return text
df["clean_text"] = df["text"].apply(clean_text)


# Step 6: Train–Test Split
from sklearn.model_selection import train_test_split

X = df["clean_text"]
y = df["label"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# Step 7: Convert Text into Numbers (TF-IDF)
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(
    stop_words="english",
    max_features=5000,
    ngram_range=(1,2)
)
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)


# Step 8: First Model — Logistic Regression (Baseline)
from sklearn.linear_model import LogisticRegression

lr_model = LogisticRegression(max_iter=1000)
lr_model.fit(X_train_tfidf, y_train)


# Step 9: Evaluation
from sklearn.metrics import confusion_matrix, classification_report

y_pred = lr_model.predict(X_test_tfidf)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))


# Step 10: Fix the Bias (This Is Real ML)
lr_model = LogisticRegression(
    max_iter=1000,
    class_weight="balanced"
)

lr_model.fit(X_train_tfidf, y_train)
y_pred = lr_model.predict(X_test_tfidf)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

print('bobo5')