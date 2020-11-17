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
from uuid import uuid4

salt = uuid4().hex


def hash_passwwd(p):
    return hashlib.sha256(salt.encode() + p.encode()).hexdigest()


def check_passwd(passwd, hash_passwd):
    return print('Вы ввели правильный пароль') if passwd == hash_passwd else print('Вы ввели не правильный пароль')


user_passwd = str(input('Введите ваш пароль:'))
hash_obj = hash_passwwd(user_passwd)
print(f'В базе хранится строка: {hash_obj}')
check_passwd(hash_passwwd(str(input('Введите ваш пароль для проверки: '))), hash_obj)
