from send_mail import postbot
from page_data import return_message

from_mail = 'lvdamaceno@hotmail.com'
to_mail = 'lvdamaceno@gmail.com'
subject = 'Mobex Watcher '
content = '<h3>Lista de Processos Disponíveis</h3><ol>'

postbot(from_mail, to_mail, subject, content, return_message())

# próximo passo encapsular isso tudo em me main
