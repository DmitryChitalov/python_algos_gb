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
from uuid import uuid4


def hash_the_object(a):
    obj = pbkdf2_hmac(hash_name='sha256',
                      password=a.encode(),
                      salt=salt.encode(),
                      iterations=100000)

    result = hexlify(obj)

    return result

def password_checker(password_hash, password):
    return password_hash == hash_the_object(password)

salt = uuid4().hex
password = input('Введите пароль:')

password_hash = hash_the_object(password)

print('В базе данных хранится строка:'.format(hash_password.decode()))

varify_password = input('Введите пароль еще раз для проверки:')

if password_checker(password_hash, varify_password):
    print('Вы ввели правильный пароль')
else:
    print('Вы ввели неправильный пароль, перепроверьте')