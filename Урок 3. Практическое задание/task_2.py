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


def check_password():
    password_1 = input('Введите пароль: ')
    salt = uuid4().hex
    hash_password_1 = hashlib.sha256(salt.encode() + password_1.encode()).hexdigest() + ':' + salt

    password_2 = input('Введите пароль ещё раз: ')
    hash_password_2 = hashlib.sha256(salt.encode() + password_2.encode()).hexdigest() + ':' + salt

    #print('Вы ввели верный пароль' if hash_password_1 == hash_password_2 else 'Вы ввели неверный пароль')
    if hash_password_1 == hash_password_2:
        print('Вы ввели верный пароль')
        return True
    else:
        print('Вы ввели неверный пароль')
        return False


check_password()