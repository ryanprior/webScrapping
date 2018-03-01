from bs4 import BeautifulSoup
import urllib

URL = 'http://lite.cnn.com/'

r = urllib.urlopen(URL).read()
soup = BeautifulSoup(r, 'html.parser')

# print soup.prettify()
# result = soup.find('div', class_='afe4286c')

headlines = [item.text for item in soup.select('div.afe4286c li a')]
headlines.sort()
print '\n'.join(headlines)


# href_tags = soup.select('div.afe4286c li a')
# print href_tags[0]['href']
# links = [item.href for item in soup.select('div.afe4286c li a')]


