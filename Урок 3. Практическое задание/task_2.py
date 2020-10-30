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

base = {'password': None, 'passwordTwo': None}

salt = 'Ivan'
b_salt = bytes(salt, 'utf-8')
hash_salt = hashlib.sha256(b_salt)
print(hash_salt.hexdigest())

def get_pass():
    base['password'] = hashlib.sha256(bytes(input('password: '), 'utf-8') + b_salt ).hexdigest()
    print(base['password'])
    base['passwordTwo'] = hashlib.sha256(bytes(input('password again: '), 'utf-8') + b_salt).hexdigest()
    print(base['password'])
    if base['password'] != base['passwordTwo']:
        print('error!')
    else:
        print('Ok')

get_pass()