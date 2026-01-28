import pandas as pd
import spacy
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Load the dataset
data = pd.read_csv("chat_data.csv")

# Display the first few records
print(data.head())


# Load SpaCy's English model
nlp = spacy.load("en_core_web_sm")

def extract_product_mentions(text):
    doc = nlp(text)
    products = [ent.text for ent in doc.ents if ent.label_ == "PRODUCT"]
    return products

# Apply the function to the messages
data['product_mentions'] = data['message'].apply(extract_product_mentions)

print(data[['message', 'product_mentions']])


# Download NLTK's VADER lexicon for sentiment analysis
nltk.download("vader_lexicon")
sia = SentimentIntensityAnalyzer()

# Define a function for sentiment analysis
def analyze_sentiment(text):
    score = sia.polarity_scores(text)
    return score['compound']

# Apply sentiment analysis to the messages
data['sentiment'] = data['message'].apply(analyze_sentiment)

print(data[['message', 'sentiment']])


# Define thresholds for positive and negative sentiment
positive_threshold = 0.5
negative_threshold = -0.5

# Identify positive and negative messages
positive_messages = data[data['sentiment'] > positive_threshold]['message']
negative_messages = data[data['sentiment'] < negative_threshold]['message']

print("Positive Messages Summary:")
for msg in positive_messages:
    print("-", msg)

print("\nNegative Messages Summary:")
for msg in negative_messages:
    print("-", msg)