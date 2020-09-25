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
from hashlib import sha256


salt = uuid4().hex.encode()


def create_hash(password):
    return sha256(salt + password.encode()).hexdigest()


def comparison(password, new_password):
    return True if password == new_password else False


password = create_hash(input('Введите пароль: '))
print(f'В базе данных хранится строка: {password}')
new_password = create_hash(input('Введите пароль еще раз для проверки: '))

if comparison(password, new_password):
    print(f'Пароли совпадают.')
else:
    print(f'Пароли не совпадают.')
