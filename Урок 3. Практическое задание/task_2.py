"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Допускаются любые усложения задания - валидация, подключение к БД, передача данных в файл
"""

import hashlib as h


def encode(inp, salt=''):
    if salt != '':
        return h.sha256((str(inp) + str(salt)).encode('utf-8')).hexdigest()
    else:
        return h.sha256(str(inp).encode('utf-8')).hexdigest()


database = {'johny': '123',
            'seigurd': '1234fsdf',
            'valeriy': 'leontiev'}

enc_data = {}

for login, password in database.items():
    enc_data[encode(login)] = encode(login, password)


def login(log, pas):
    if encode(log) in enc_data.keys():
        if encode(log, pas) in enc_data.values():
            return 'You have been succesfully logged in'
        else:
            return 'Password is not correct. Please check it again.'
    else:
        return 'Login does not exist'


def login_attempt():
    a = str(input('Enter your login: '))
    b = str(input('Enter your password: '))
    print(login(a, b))


login_attempt()
