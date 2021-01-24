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

Допускаются любые усложения задания - валидация, подключение к БД, передача данных в файл
"""
import hashlib
from uuid import uuid4


def check_pass(first_hash, second):
    return (hashlib.sha256(salt.encode() + second.encode()).hexdigest()) == first_hash


salt = uuid4().hex
print(salt)

first_try = input("Введите пароль: ")
res1 = hashlib.sha256(salt.encode() + first_try.encode()).hexdigest()
print(res1)

second_try = input("Пожалуйста, повторите пароль: ")
res2 = hashlib.sha256(salt.encode() + second_try.encode()).hexdigest()
print(res2)
if check_pass(res1, second_try):
    print("Вы ввели верный пароль")
else:
    print("Введенный пароль неверен")
