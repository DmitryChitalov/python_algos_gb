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


def hash_password(password):
    salt = uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt


def check_hash_password(password, hash):
    arr = hash.split(":")
    salt = str(arr[1])
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt == hash


def save_to_file(hash, path):
    pass_file = open(path, 'w')
    pass_file.write(hash)
    pass_file.close()


def get_from_file(path):
    pass_file = open(path, 'r')
    stored_hash = pass_file.read()
    pass_file.close()
    return stored_hash


path = './pass.txt'

password = input('Введите пароль:')
hash = hash_password(password)
save_to_file(hash, path)
password_repeat = input('Введите пароль еще раз для проверки:')
stored_hash = get_from_file(path)
if check_hash_password(password_repeat, stored_hash):
    print('Вы ввели правильный пароль')
else:
    print('Вы ввели неправильный пароль')
