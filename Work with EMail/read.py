import imaplib
import email
from email.header import decode_header
import webbrowser
import os

# учетные данные
username = "address@gmail.com"
password = "password"

def clean(text):
    # чистый текст для создания папки
    return "".join(c if c.isalnum() else "_" for c in text)
	
# создаем класс IMAP4 с SSL 
imap = imaplib.IMAP4_SSL("imap.gmail.com")
# аутентифицируем
imap.login(username, password)

status, messages = imap.select("INBOX")
# количество популярных писем для получения
N = 3

# общее количество писем
messages = int(messages[0])

for i in range(messages, messages-N, -1):
    # получаем сообщение электронной почты по идентификатору
    res, msg = imap.fetch(str(i), "(RFC822)")
    for response in msg:
        if isinstance(response, tuple):
            # анализируем байтовое электронное письмо в объект сообщения
            msg = email.message_from_bytes(response[1])
            # расшифроваем тему письма
            subject, encoding = decode_header(msg["Subject"])[0]
            if isinstance(subject, bytes):
                # если это байты, декодируем в строку
                subject = subject.decode(encoding)
            # расшифровываем отправителя электронной почты
            From, encoding = decode_header(msg.get("From"))[0]
            if isinstance(From, bytes):
                From = From.decode(encoding)
            print("Subject:", subject)
            print("From:", From)
            # если сообщение электронной почты составное
            if msg.is_multipart():
                # перебираем части письма
                for part in msg.walk():
                    # извлекаем тип содержимого электронной почты
                    content_type = part.get_content_type()
                    content_disposition = str(part.get("Content-Disposition"))
                    try:
                        # получаем содержимое письма
                        body = part.get_payload(decode=True).decode()
                    except:
                        pass
                    if content_type == "text/plain" and "attachment" not in content_disposition:
                        # печатаем текст/обычные электронные письма и пропускаем вложения
                        print(body)
                    elif "attachment" in content_disposition:
                        # скачиваем вложение
                        filename = part.get_filename()
                        if filename:
                            folder_name = clean(subject)
                            if not os.path.isdir(folder_name):
                                # создаем папку для этого электронного письма (названную в соответствии с темой)
                                os.mkdir(folder_name)
                            filepath = os.path.join(folder_name, filename)
                            # скачиваем вложение и сохраняем его
                            open(filepath, "wb").write(part.get_payload(decode=True))
            else:
                # извлекаем тип содержимого электронной почты
                content_type = msg.get_content_type()
                # получаем содержимое письма
                body = msg.get_payload(decode=True).decode()
                if content_type == "text/plain":
                    # печатаем только текстовые части электронного письма
                    print(body)
            if content_type == "text/html":
                # если это HTML, создаем новый HTML-файл и открываем его в браузере
                folder_name = clean(subject)
                if not os.path.isdir(folder_name):
                    # создаем папку для этого электронного письма (названную в соответствии с темой)
                    os.mkdir(folder_name)
                filename = "index.html"
                filepath = os.path.join(folder_name, filename)
                # пишем файл
                open(filepath, "w").write(body)
                # открываем в браузере по умолчанию
                webbrowser.open(filepath)
            print("="*100)
# закрываем соединение и выходим из системы
imap.close()
imap.logout()