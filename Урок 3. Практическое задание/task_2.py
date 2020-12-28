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

import time
import hashlib


def check_password():
    user_password = input('Введите пароль: ')
    salt = str(time.time())  # salt

    hash_pass = hashlib.sha256(user_password.encode() + salt.encode()).hexdigest()
    print('Созданный хеш: ' + hash_pass)

    user_check_password = input('Введите пароль для проверки: ')
    hash_check_pass = hashlib.sha256(user_check_password.encode() + salt.encode()).hexdigest()

    if hash_pass == hash_check_pass:
        print('Пароли совпадают')
    else:
        print('Вы ввели неправильный пароль')


check_password()
