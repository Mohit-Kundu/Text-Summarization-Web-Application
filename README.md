# Text-Summarization-with-Python
This is an extractive text summarizer built using **python** and **flask**, that takes a url, generates a summary and then displays the estimated time to read the summary.

## How do I run it?
1. Run app.py
2. Click on the link on the displayed in the terminal
3. Paste the url of the article in the url field.
4. Click the Summarize button to get a summary.

## How does it work?
- Upon receiving a url, scraper.py scrapes the text present on the website. The text is then formatted and cleant.
- This formatted text is then passed to the summarizer.py which uses spacy  tokenizes the text into sentences and words.
- The frequency of each word is calculated and stored in a dictionary. The frequency of each word is then normalized by dividing by the maximum frequency (this is done in order to find the relative frequency of each word).
- Next, the sentence scores are calculated by adding the word frequency of each word present in the sentence.
- A heap queue is then used to get sentences with the highest sentence scores.
- The sentences are then joined to get the summary.
- Next, the estimated reading time is calculated.
- Finally, the title, summary and estimated reading time are displayed.


## Requirements
- Python version >= 3.0
- Spacy v3.10
- Flask
- Beautiful Soup v4.0 or above

## Screenshots
![Text Summarizer](screenshots/text-summarizer.gif)
