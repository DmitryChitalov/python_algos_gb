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
from hashlib import pbkdf2_hmac
from binascii import hexlify
from uuid import uuid4

#Вариант1


user_login = input('Введите логин: ')
user_password = input('Введите пароль: ')
user_login = user_login.encode('utf8')
user_password = user_password.encode('utf8')

obj = pbkdf2_hmac(hash_name='sha256',
                  password=bytes(user_password),
                  salt=bytes(user_login),
                  iterations=1000)

user_login1 = input('Введите логин: ')
user_password1 = input('Введите пароль: ')
user_login1 = user_login1.encode('utf8')
user_password1 = user_password1.encode('utf8')

obj1 = pbkdf2_hmac(hash_name='sha256',
                  password=bytes(user_password1),
                  salt=bytes(user_login1),
                  iterations=1000)

print(obj == obj1)

#Вариант2
import hashlib

salt = uuid4().hex

us_password = input('Введите пароль: ')
result = hashlib.sha256(salt.encode() + us_password.encode()).hexdigest()
us_password1 = input('Введите пароль еще раз для проверки: ')
result1 = hashlib.sha256(salt.encode() + us_password1.encode()).hexdigest()
print(f'В базе данных хранится строка: {result}')
if result == result1:
    print('Пароли совпадают')
else:
    print('Пароли не совпадают')

