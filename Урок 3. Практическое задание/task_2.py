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

password = input('Введите пароль: ').strip().encode('Utf-8')
salt = uuid4().bytes

mem_password = hexlify(pbkdf2_hmac(hash_name='sha256', password=password, salt=salt, iterations=100000))

repeat_password = input('Введите пароль еще раз для проверки: ').strip().encode('Utf-8')

mem_repeat = hexlify(pbkdf2_hmac(hash_name='sha256', password=repeat_password, salt=salt, iterations=100000))

if mem_password == mem_repeat:
    print('Вы ввели правильный пароль')
else:
    print('Пароли не совпадают')
