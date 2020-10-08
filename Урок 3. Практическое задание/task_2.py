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


def check_pwd():
    import hashlib
    from uuid import uuid4

    salt = uuid4().hex
    passwd1 = (input("Please input password: "))
    passwd2 = (input("Please input password again: "))
    hex_dig_res1 = hashlib.sha256(salt.encode() + passwd1.encode('UTF-8')).hexdigest()
    hex_dig_res2 = hashlib.sha256(salt.encode() + passwd2.encode('UTF-8')).hexdigest()
    if hex_dig_res1 == hex_dig_res2:
        print("Access allowed")
    else:
        print("Access denied")


check_pwd()
