# pip install requests
# pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup

url = 'http://ciac.ufpa.br/index.php/mobilidade-academica'
url_base = 'http://ciac.ufpa.br'


def capture_page(url):
    p = requests.get(url)
    return p


def parse_page():
    # Faz o parse da página e cria um objeto BeatifulSoup como uma estrutura de dados aninhada
    soup = BeautifulSoup(capture_page(url).text, 'html.parser')
    # Captura todas as instâncias da cat-children
    processes = soup.find_all(class_='cat-children')
    # Captura todas as instâncias da tag ul
    ul = processes[0].find_all('ul')
    # Captura todas as instâncias da tag li
    li = ul[0].find_all('li')

    return li


def return_list():
    i = 0
    li = parse_page()
    for l in li:
        # Percorre a lista e printa cada posição formatada para leitura
        year = li[i].find('a').text
        articles = li[i].find('dt').text
        total = li[i].find('dd').text
        link = li[i].find('a')['href']

        print(year.strip())
        print(articles.strip(), total.strip())
        print(url_base + link.strip())
        print(' ')

        i = i + 1

return_list()
