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
data_urls = {}
salt = uuid4().hex
password = input("Введите пароль: ")
res = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
print(f"В базе данных хранится строка: {res}")


def check_in(res_password):
    password_check = input("Введите пароль еще раз для проверки: ")
    res_check = hashlib.sha256(salt.encode() + password_check.encode()).hexdigest()
    if res_password == res_check:
        print("Вы ввели правильный пароль!")
        return
    else:
        print("Пароль не верный, попробуйте еще раз")
        check_in(res_password)


check_in(res)
