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


def pwd_hash(pwd, salt):
    return hashlib.sha256(pwd.encode() + salt.encode()).hexdigest()


if __name__ == '__main__':
    login = input('login: ')
    encrypt_pwd = pwd_hash(input('type password: '), login)

    print(f'Password hash is: {encrypt_pwd}')

    if encrypt_pwd == pwd_hash(input('re-type password: '), login):
        print('Correct password')
