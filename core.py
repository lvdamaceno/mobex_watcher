'''
pip install requests
pip install beautifulsoup4
'''

import requests
from bs4 import BeautifulSoup

url = 'http://ciac.ufpa.br/index.php/mobilidade-academica'
url_base = 'http://ciac.ufpa.br'
page = requests.get(url)
# print(page)
# print(page.status_code)
# print(page.text)


soup = BeautifulSoup(page.text, 'html.parser')
processes = soup.find_all(class_='cat-children')
ul = processes[0].find_all('ul')
li = ul[0].find_all('li')

i = 0
for l in li:
    year = li[i].find('a').text
    articles = li[i].find('dt').text
    total = li[i].find('dd').text
    link = li[i].find('a')['href']

    print(year.strip())
    print(articles.strip(), total.strip())
    print(url_base + link.strip())
    print(' ')

    i = i + 1
