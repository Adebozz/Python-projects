import requests
from bs4 import BeautifulSoup
import operator

def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code)
    for post_text in soup.findAll('a', {'class': 'index_singleListeningTitles'}):
        content = post_text.string
        words = content.lower().split()
        for each_word in words:
            word_list.append(each_word)
        clean_up_list(word_list)

def clean_up_list(word_list):
    clear_word_list = []
    for word in word_list:
        symbols = "!£$%^&*(()_+-='{}:@~<>?,./;'#]['"
        for s in range(1, len(symbols)):
            word = word.replace(symbols[1], "")
        if len(word) > 0:
            print(word)
            clear_word_list.append(clear_word_list)
    create_dictionary(clear_word_list)
def create_dictionary(clear_word_list):
    word_count = ()
    for word in clear_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
        print(key, value)
        
start('')