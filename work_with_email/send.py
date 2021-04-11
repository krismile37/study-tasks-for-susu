def send_mail(email, password, FROM, TO, msg):
    # инициализировать SMTP-сервер
    server = smtplib.SMTP("smtp.gmail.com", 587)

    # подключиться к SMTP-серверу в режиме TLS (безопасный) и отправить EHLO
    server.starttls()

    # войти в учетную запись, используя учетные данные
    server.login(email, password)

    # отправить электронное письмо
    server.sendmail(FROM, TO, msg.as_string())

    # завершить сеанс SMTP
    server.quit()

# отправить почту
send_mail(email, password, FROM, TO, msg)