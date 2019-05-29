import requests
from bs4 import BeautifulSoup

url = 'http://www.ceps.ufpa.br/'


def parse_page(u):
    # Faz o parse da página e cria um objeto BeatifulSoup como uma estrutura de dados aninhada
    soup = BeautifulSoup(requests.get(u).text, 'html.parser')
    mobilidades = soup.find_all(class_='je_acc', id="je_accord306")
    anos = mobilidades[0].find_all('li')
    links = anos[0].find_all('a')

    return links


def list_ceps():
    links = parse_page(url)
    mail_message = []
    for link in links:
        text = link.text
        link = url + link['href']
        mail_message.append('<li>' + text + '</li>' +
                            '<ul>' + link + '</ul>')

    return ''.join(mail_message)
