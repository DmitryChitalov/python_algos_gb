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

def get_hash(pass_new):
    return hashlib.sha256(salt.encode() + pass_new.encode()).hexdigest()

def hash_check(hash_pass, old_pass):
    if hash_pass == hashlib.sha256(salt.encode() + old_pass.encode()).hexdigest():
        return True
    else:
        return False

new_pass = input('Введите пароль: ')
hash_pass = get_hash(new_pass)
print(f'В базе данных хранится строка: {hash_pass}')

old_pass = input('Введите пароль еще раз для проверки: ')

if hash_check(hash_pass, old_pass) == True:
    print('Вы ввели правильный пароль')
else:
    print('Внимание! Пароли не совпадают')
