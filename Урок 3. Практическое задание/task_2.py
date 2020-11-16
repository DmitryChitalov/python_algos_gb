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


def hash_gen(password):
    salt = uuid4().hex
    result = hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
    return result

def hash_check(hashed_password, second_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + second_password.encode()).hexdigest()


first_input = input('Please enter your password: ')
hashed_password = hash_gen(first_input)
print('The password we have in our DB is: ' + hashed_password)
second_input = input('Please enter your password once again: ')

if hash_check(hashed_password, second_input):
    print('Password is correct.')
else:
    print('Well well well, look at the hacker we have here!')

