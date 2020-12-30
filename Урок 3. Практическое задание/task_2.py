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
import random
import hashlib


def salt_gen(len = 10):
    return "".join(random.choice("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") for i in  range(len))

SALT = salt_gen(16)

passwd = input("Введите пароль ")
res = hashlib.sha256(SALT.encode() + passwd.encode()).hexdigest()
print(f"Созданный хэш {res}")
user_input = input("Введите пароль для проверки ")
user_input = hashlib.sha256(SALT.encode() + user_input.encode()).hexdigest()
print(f"Сверяемся с созданным хэшэм {user_input}")
if res == user_input:
    print("Вы ввели правильный пароль!")
else:
    print("Вы ввели неправильный пароль!")




