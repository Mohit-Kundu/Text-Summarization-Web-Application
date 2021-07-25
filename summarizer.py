import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from scraper import scraper

stopwords = list(STOP_WORDS)
print(stopwords)

nlp = spacy.load('en_core_web_sm')

# Scraping text from article
text = scraper('https://en.wikipedia.org/wiki/Natural_language_processing')

# Saving tokenized sentence
doc = nlp(text)

tokens = [token.text for token in doc]
#print(tokens)

# Finding Word Frequencies
word_frequencies = {}

for word in doc:
    if word.text.lower() not in stopwords:
        if word.text.lower() not in punctuation:
            if word.text.lower() not in word_frequencies.keys():
                #Adding new word to word_freequeny
                word_frequencies[word.text.lower()] = 1
            else:
                word_frequencies[word.text.lower()] += 1

print(word_frequencies)
