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

from uuid import uuid4
import hashlib
import secrets


def pass_hash(passwd):
    return hashlib.sha256(salt.encode() + passwd.encode()).hexdigest()


salt = uuid4().hex
user_passwrd = input('Введите пароль: ')
hash_passwrd = pass_hash(user_passwrd)
print(f'В базе данных хранится строка: {hash_passwrd}')

user_passwrd1 = input('Введите пароль еще раз для проверки: ')
hash_passwrd1 = pass_hash(user_passwrd1)

if secrets.compare_digest(hash_passwrd, hash_passwrd1):
    print('Вы ввели правильный пароль')
else:
    print('Внимание! Пароли не совпадают')
