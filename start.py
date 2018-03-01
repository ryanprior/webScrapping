from bs4 import BeautifulSoup
import urllib.request
from py_thesaurus import Thesaurus
from random import shuffle

URL = 'http://lite.cnn.com/'

r = urllib.request.urlopen(URL).read()
soup = BeautifulSoup(r, 'html.parser')

headlines = [item.text for item in soup.select('div.afe4286c li a')]
shuffle(headlines)


def maybe_synonym(word):
    synonyms = Thesaurus(word).get_synonym()
    if(len(synonyms) is 0):
        return word
    else:
        return synonyms[0]

random = headlines[0]
print(random)
print(' '.join([maybe_synonym(word) for word in random.split(' ')]))


