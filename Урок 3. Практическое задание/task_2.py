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
import os
from hashlib import pbkdf2_hmac
from binascii import hexlify

my_salt = os.urandom(32)


def password_entry():
    password = input('Введите пароль: ')
    password_hash = pbkdf2_hmac(hash_name='sha256', password=password.encode(), salt=my_salt, iterations=100000)
    return hexlify(password_hash)


def password_verification(passwd):
    password = input('Введите пароль еще раз для проверки: ')
    password_hash = pbkdf2_hmac(hash_name='sha256', password=password.encode(), salt=my_salt, iterations=100000)
    print(hexlify(password_hash))
    if passwd == hexlify(password_hash):
        print('Вы ввели правильный пароль')
    else:
        print('Вы ввели неправильный пароль')


if __name__ == '__main__':
    password_hash_all = password_entry()

    print(f'hash пароля: {password_hash_all}')

    password_verification(password_hash_all)
