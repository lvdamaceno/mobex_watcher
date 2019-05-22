import requests
from bs4 import BeautifulSoup

url = 'http://ciac.ufpa.br/index.php/mobilidade-academica'
url_base = 'http://ciac.ufpa.br'


def parse_page(u):
    # Faz o parse da página e cria um objeto BeatifulSoup como uma estrutura de dados aninhada
    soup = BeautifulSoup(requests.get(u).text, 'html.parser')
    # Captura todas as instâncias da cat-children que na página é a lista de itens
    processes = soup.find_all(class_='cat-children')
    # Captura todas as instâncias da tag ul que na página é cada item da lista
    tag_ul = processes[0].find_all('ul')
    # Captura todas as instâncias da tag li me da acesso aos dados de interesse
    tag_li = tag_ul[0].find_all('li')

    return tag_li


def return_message():
    page_content = parse_page(url)
    mail_message = []
    for item in page_content:
        year = item.find('a').text.strip()
        articles = item.find('dt').text.strip()
        total = item.find('dd').text.strip()
        link = url_base + item.find('a')['href'].strip()
        mail_message.append('<li>' + year + '</li>' +
                            '<ul>' +
                            '<li>' + link + '</li>' +
                            '<li>' + articles + total + '</li>' +
                            '</ul>')
    return ''.join(mail_message)
