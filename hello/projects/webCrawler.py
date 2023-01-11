import requests
from bs4 import BeautifulSoup

def movies_spider(max_pages):
    page = 1
    while page < max_pages:
        url = 'https://www.thenetnaija.net/videos/movies' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a', {'h2'}):
            href = link.get('href')
            print(href)
        page += 1

movies_spider(1)
