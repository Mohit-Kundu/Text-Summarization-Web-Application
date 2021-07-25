import bs4 as bs
import urllib.request
import re

def scraper(url):
    article_text = ""

    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

    '''url = "https://www.newscientist.com/article/2284533-flexible-computer-processor-is-the-most-powerful-plastic-chip-yet/"
    url = "https://edition.cnn.com/world/live-news/tokyo-2020-olympics-07-23-21-spt/h_3fc99ad3b8f8dd82ac977487dae0f194"'''
    headers={'User-Agent':user_agent,} 

    request=urllib.request.Request(url,None,headers) #The assembled request
    response = urllib.request.urlopen(request)
    data = response.read() # The data u need

    parsed_article = bs.BeautifulSoup(data, 'lxml')

    paragraphs = parsed_article.find_all('p')

    for p in paragraphs:
        article_text += p.text

    # Removing Square Brackets and Extra Spaces
    def remove_square_brackets_and_extra_spaces(article_text):
        article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
        return re.sub(r'\s+', ' ', article_text)

    # Removing special characters and digits
    def remove_spl_chars_and_digits(article_text):
        formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text)
        return re.sub(r'\s+', ' ', formatted_article_text)

    string = remove_square_brackets_and_extra_spaces(article_text)
    body = remove_spl_chars_and_digits(article_text)
    return body
