import spacy

nlp  = spacy.black("pt")
stopwords = nlp.Defaults.stop_words

print(stopwords)