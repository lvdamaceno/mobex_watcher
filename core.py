# pip install requests
# pip install beautifulsoup4
# pip install sendgrid

import requests
from bs4 import BeautifulSoup
from mail import send_message

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
    list = []
    for l in li:
        # Percorre a lista
        year = li[i].find('a').text
        articles = li[i].find('dt').text
        total = li[i].find('dd').text
        link = li[i].find('a')['href']

        list.append('<li>' + year.strip() + ' <br />' + (url_base + link.strip())
                    + ' <br />' + articles.strip() + total.strip() + '</li><br />')

        i = i + 1

    return list


mensagem = ''.join(return_list())

send_message('Mobex Watcher', '<h3>Lista de Processos</h3><ol>' + mensagem + '</ol>')
