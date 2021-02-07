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

database_dict = {}
salt = uuid4().hex

passwd = input('Введите пароль: ')


resulting_hash = hashlib.sha256(salt.encode() + passwd.encode()).hexdigest()
database_dict[0] = resulting_hash

for _ in range(3):
    check_passwd = input('Введите пароль повторно: ')
    check_passwd_hash = hashlib.sha256(salt.encode() + check_passwd.encode()).hexdigest()
    database_dict[1] = check_passwd_hash
    if database_dict[0] == database_dict[1]:
        print('Успех!Вы ввели правильный пароль')
        break
    else:
        print('Пароли не совпадают.')
print('Вы использовали слишком много попыток, повторите аутентификацию позже')
