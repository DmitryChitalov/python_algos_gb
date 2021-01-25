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

from hashlib import sha1
from uuid import uuid4


def password():
    salt = uuid4().hex
    user_password = input('Enter password: ')
    return check_password(salt, user_password)


def check_password(salt, origin_password):
    first_try = sha1(salt.encode() + origin_password.encode('utf-8')).hexdigest()
    print(first_try)
    user_password = input('Enter password again: ')
    second_try = sha1(salt.encode() + user_password.encode('utf-8')).hexdigest()
    print(second_try)
    if first_try == second_try:
        print('Check correct!')
    else:
        print('Error in password!')


password()
