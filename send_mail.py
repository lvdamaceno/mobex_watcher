import os
import datetime
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

now = datetime.datetime.now()


def postbot(from_mail, to_mail, subject, content, message):
    # script para o envio do e-mail via sendgrid
    message = Mail(
        from_email=from_mail,
        to_emails=to_mail,
        subject=subject + str(now),
        html_content=content + message + '</ol>')
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)
