Building a Text Analyzer with Python and Natural Language Processing (NLP)
28-Dec-2024

https://python.plainenglish.io/building-a-text-analyzer-with-python-and-natural-language-processing-nlp-6b7d327a5b1a

~/miniconda3/bin/conda
source ~/miniconda3/bin/activate

IMPORTANT
could not get this working with .venv
therefore used Conda


import spacy
import nltk
click import package

python -m spacy download en_core_web_sm


NLP
gives the ability to understand and work w/ human language


NLTK
Natural Language ToolKit
basic text analyzer
extract keywords, perform sentiment analysis
create simple text summaries


en_core_web_sm
model for SpaCy
lightweight model w/ vocabulary syntax and
entities making it ideal for general purpose NLP tasks

others
en_core_web_md
en_core_web_lg

additional word vectors that provide better accuracy for tasks
requiring more context or detail


Step 1: Creating a Fake Chat Dataset
message firld is main target for analysis


Step 2: Loading the Dataset and Preparing for Analysis
use pandas and display data loaded OK


Step 3: Analyzing Product Mentions with SpaCy
extract keywords e.g. "TechWidget" from each message
use SpaCy
init SpaCy model and define function to extract product mentions

extract_product_mentions
processes each message to identify entities classified as products


Step 4: Performing Sentiment Analysis with NLTK
Sentiment analysis helps maintain emotional tone of each message

VADER
Valence Aware Dictionary and Sentiment Reasoner
ideal for analyzing short informal text like chat messages
e.g.
SentimentIntensityAnalyzer
code calculates a sentiment score for each message

compound score provides an overall sentiment rating btwn -1 and +1


Step 5: Summarizing Messages
create simple summary by focusing on messages with high or low
sentiment scores - extremes often represent most enthusiasitc
or critical opinions

code filters messages based on sentiment scores
msgs > 0.5 = positive
msgs < 0.5 = negative


Step 6: Running the Text Analyzer
display each message along w/ identified product mentions and
sentiment scores
+ve and -ve offer insignhts into user feedback trends