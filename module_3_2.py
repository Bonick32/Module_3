def send_email(message, recipient, sender = "university.help@gmail.com"):
    relevant = ['@', '.com', '.ru', '.net']
    dog1 = recipient[recipient.rfind('@'):recipient.rfind('@') + 1]
    dog2 = sender[sender.rfind('@'):sender.rfind('@') + 1]
    dut1 = recipient[recipient.rfind('.'):]
    dut2 = sender[sender.rfind('.'):]

    if dut1 and dut2 not in relevant:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif dog2 and dog1 not in relevant:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient} - некорректно указан email' )
    else:
        if recipient == sender:
            print('Невозможно отправить письмо самому себе!')
        else:
            if sender == "university.help@gmail.com":
                print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
            else:
                print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
send_email('Это сообщение для проверки связи', 'vasyok1337_gmail.com')