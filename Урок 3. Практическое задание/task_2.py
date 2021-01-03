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
"""

import hashlib

auth_obj = {
    'user': 'admin',
    'password': '1234'
}


def get_hash(login_salt, passw):
    return hashlib.sha3_256((login_salt + ':' + passw).encode('UTF-8')).hexdigest()


auth_hash = (get_hash(auth_obj['user'], auth_obj['password']))


def check_auth(login, new_passw):
    return auth_hash == hashlib.sha3_256((login + ':' + new_passw).encode('UTF-8')).hexdigest()


login = input('Введите логин!')
password = input('Введите пароль: ')
if check_auth(login, password):
    print('Вы вошли в систему!')
else:
    print('Неверный логин/пароль!')