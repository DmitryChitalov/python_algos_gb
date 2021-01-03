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

salt = uuid4().hex
print(salt)


def get_hash(password):
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest()


def hash_check(hashed_password, check_password):
    return hashed_password == hashlib.sha256(salt.encode() + check_password.encode()).hexdigest()


password = input('Введите пароль: ')
hashed_password = get_hash(password)
print(f'Созданный хэш: {hashed_password}')

check_password = input('Введите пароль повторно: ')

if hash_check(hashed_password, check_password):
    print('Верный пароль')
else:
    print('Не верный пароль')
