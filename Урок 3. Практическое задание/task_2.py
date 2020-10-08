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
from hashlib import pbkdf2_hmac
from binascii import hexlify


def input_pass():
    user_pass = input('Введите пароль:')
    salt = 'Введите пароль:'

    obj = pbkdf2_hmac(hash_name='sha256',
                      password=user_pass.encode('utf-8'),
                      salt=salt.encode('utf-8'),
                      iterations=100000)
    print(hexlify(obj))
    return obj


a = input_pass()
b = input_pass()

if a == b:
    print('Вы ввели правильный пароль')
else:
    print('Пароль введен не верно')
