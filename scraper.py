import bs4 as bs
import urllib.request
import re

'''Removes the citations and square brackets in super script'''
def remove_brackets(text):
        text = re.sub(r'\[[0-9]*\]', ' ', text)
        return re.sub(r'\s+', ' ', text)

'''Calculating reading speed by dividing text length by average reading speed'''
def estimated_reading_time(text):
    reading_time = int(len(text)/200)
    return reading_time

'''Scrapes content from paragraph and div tags of website'''
def scraper(url):
    article_text = ""

    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers={'User-Agent':user_agent,} 

    request=urllib.request.Request(url,None,headers)
    response = urllib.request.urlopen(request)
    data = response.read()

    parsed_article = bs.BeautifulSoup(data, 'lxml')

    title = parsed_article.find('title').text

    paragraphs = parsed_article.find_all('p')

    # Checking content of p tags
    if len(paragraphs) != 0:
        for p in paragraphs:
            article_text += p.text
    
    # Checking content of div tags
    else:
        divs = parsed_article.find_all('div', id = 'container')

        for div in divs:
            article_text += div.text

    body = remove_brackets(article_text)
        
    return title, body