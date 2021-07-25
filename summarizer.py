import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from scraper import scraper

stopwords = list(STOP_WORDS)
#print(stopwords)

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
                # Adding new word to word_frequency
                word_frequencies[word.text.lower()] = 1
            else:
                # Incrementing frequency in word already exists
                word_frequencies[word.text.lower()] += 1

#print(word_frequencies)

# Normalizing Frequencies
max_frequency = max(word_frequencies.values())
#print(max_frequency)

for word in word_frequencies.keys():
    word_frequencies[word] /= max_frequency

#print(word_frequencies)

# Sentence Tokenization
sentence_tokens = [sent for sent in doc.sents]
#print(sentence_tokens)

# Calculating sentence scores
sentence_scores = {}

for sent in sentence_tokens:
    for word in sent:
        if word.text.lower() in word_frequencies.keys():
            if sent not in sentence_scores.keys():
                sentence_scores[sent] = word_frequencies[word.text.lower()]
            else:
                sentence_scores[sent] += word_frequencies[word.text.lower()]

print(sentence_scores)


