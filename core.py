import datetime
from send_mail import postbot
from ciac import list_ciac
from ceps import list_ceps

now = datetime.datetime.now()

from_mail = 'lvdamaceno@hotmail.com'
to_mail = 'lvdamaceno@gmail.com'
subject = 'Mobex Watcher '
content = '<h3>Lista de Processos Disponíveis</h3><ol>'

postbot(from_mail, to_mail, subject + now.strftime('%x'),
        '<h3>Lista de Processos Disponíveis CIAC</h3><ol>', list_ciac())
postbot(from_mail, to_mail, subject + now.strftime('%x'),
        '<h3>Lista de Processos Disponíveis CEPS</h3><ol>', list_ceps())

# próximo passo encapsular isso tudo em um main
