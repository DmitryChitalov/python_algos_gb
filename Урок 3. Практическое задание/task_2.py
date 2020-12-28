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
import uuid


def auth():
    password = input("Введите пароль: ")
    salt = uuid.uuid4().hex

    hash = hashlib.sha256(salt.encode("utf-8") + password.encode("utf-8")).hexdigest()

    with open("db.txt", "w") as f:
        f.write(f"{hash}")

    print(f"В БД записано: {hash}")

    confirm_password = input("Введите пароль еще раз для проверки: ")
    confirm_hash = hashlib.sha256(salt.encode("utf-8") + confirm_password.encode("utf-8")).hexdigest()

    with open("db.txt", "r") as f:
        hash = f.readline()

        if hash == confirm_hash:
            print("Вы ввели правильный пароль")
        else:
            print("Вы ввели неправильный пароль")


auth()
