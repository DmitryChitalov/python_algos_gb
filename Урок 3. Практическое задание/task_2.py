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

################################################################
from binascii import hexlify
from hashlib import pbkdf2_hmac

################################################################
db = dict()

################################################################
while True:
    login = input('Enter login: ')
    if login == "0":
        exit(0)
    if login in db.keys():
        print(f"welcome {login}")
        password = input('Enter password: ')
        password_hash = pbkdf2_hmac(hash_name='sha256',
                                    password=password.encode(),
                                    salt=login.encode(),
                                    iterations=100000)
        print(password_hash)
        print(db[login].get("hashed_password"))
        if hexlify(password_hash) != db[login].get("hashed_password"):
            print("see your later")
            continue
        print(f"Like to see you, {login}")
    else:
        print(f"welcome new user {login}")
        password = input('Enter password: ')
        password_hash = pbkdf2_hmac(hash_name='sha256',
                                    password=password.encode(),
                                    salt=login.encode(),
                                    iterations=100000)
        print(password_hash)
        db[login] = {"hashed_password": hexlify(password_hash)}
    print(db)
    print((db[login].values()))
################################################################
