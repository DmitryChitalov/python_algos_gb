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

user_email = input('Введите адрес электронной почты: ')
user_password = input('Придумайте пароль: ')
salt = user_email
stored_pass = hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()


def check_password():
    enter_email = input('Введите ваш адрес электронной почты: ')
    enter_password = input("Введите ваш пароль: ")
    try_pass = hashlib.sha256(enter_email.encode() + enter_password.encode()).hexdigest()
    if try_pass == stored_pass:
        print('Пароль верный')
    else:
        print('Неверный пароль')

check_password()
