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

salt = uuid4().hex

def get_hash(pass_obj):
    return hashlib.sha256(salt.encode() + pass_obj.encode()).hexdigest()

def check_hash(pass_hash, user_pass):
    return pass_hash == hashlib.sha256(salt.encode() + user_pass.encode()).hexdigest()

print('Program "Check hash"')
input_pass = input('Please enter a password: ')
hash_obj = get_hash(input_pass)
print(f'Hash for pass is : {hash_obj}')

check_pass = input('Please enter a early password: ')

if check_hash(hash_obj, check_pass):
    print('Passwords is match')
else:
    print('Passwords is NOT match')

