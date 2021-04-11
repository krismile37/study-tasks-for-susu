import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from bs4 import BeautifulSoup as bs

# ваши учетные данные
email = "address@gmail.com"
password = "password"

# электронная почта отправителя
FROM = "from address@gmail.com"

# адрес электронной почты получателя
TO   = "to address@gmail.com"

# тема письма (тема)
subject = "Just a subject"

# инициализируем сообщение, которое хотим отправить
msg = MIMEMultipart("alternative")

# установить адрес электронной почты отправителя
msg["From"] = FROM

# установить адрес электронной почты получателя
msg["To"] = TO

# задаем тему
msg["Subject"] = subject

# установить тело письма как HTML
html = """
This email is sent using <b>Python</b>!
"""
# делаем текстовую версию HTML
text = bs(html, "html.parser").text

# установить тело письма как HTML
html = open("mail.html").read()

# делаем текстовую версию HTML
text = bs(html, "html.parser").text

text_part = MIMEText(text, "plain")
html_part = MIMEText(html, "html")

# прикрепить тело письма к почтовому сообщению
# сначала прикрепите текстовую версию
msg.attach(text_part)
msg.attach(html_part)

print(msg.as_string())