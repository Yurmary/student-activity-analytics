import smtplib
from email.message import EmailMessage

def send_email(subject, body):
    smtp_server = "smtp.mail.ru"
    port = 465  # стандартный порт для SMTP_SSL

    sender_email = "yurinok.mary@mail.ru"
    receiver_email = "yurinok@list.ru"
    password = "zVtjhSEgeCGpRi04eQLp"  # используйте пароль для приложений

    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.send_message(msg)
