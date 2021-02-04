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

import uuid
import hashlib
from binascii import hexlify


def hash_pwd(password):
    salt = uuid.uuid4().hex
    # return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
    obj = str(hexlify(hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100000))) + ':' + salt
    return obj


def check_pwd(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    # return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()
    obj = hashlib.pbkdf2_hmac('sha256', user_password.encode(), salt.encode(), 100000)
    return password == str(hexlify(obj))


new_pwd = input("Введите пароль:")
hashed_pwd = hash_pwd(new_pwd)
print("В базе данных хранится строка:" + hashed_pwd)
f = open('pwd.txt', 'w')
f.write(hashed_pwd + '\n')
f.close()
new_pwd2 = input("Введите пароль еще раз для проверки:")

if check_pwd(hashed_pwd, new_pwd2):
    print("Correct password!")
else:
    print("Wrong password!")
