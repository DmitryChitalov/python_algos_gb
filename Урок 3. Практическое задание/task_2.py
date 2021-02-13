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


def f_ch_pass():
    v_pass = input('Enter password: ')
    salt = uuid4().hex
    hash_pass = hashlib.sha256(salt.encode() + v_pass.encode()).hexdigest() + ':' + salt

    v_pass_2 = input('Enter password one more time: ')
    hash_pass_2 = hashlib.sha256(salt.encode() + v_pass_2.encode()).hexdigest() + ':' + salt

    if hash_pass == hash_pass_2:
        print('Correct password')
        return True
    else:
        print('Incorrect password')
        return False


f_ch_pass()
