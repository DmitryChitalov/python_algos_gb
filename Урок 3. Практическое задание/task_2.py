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
from hashlib import sha256

login = input("Ваш логин: ")
password = input("Ваш пароль: ")


def hash1(passw):
    hash_obj1 = sha256(f"mw238v32{passw}87s3gi2d".encode("utf-8"))
    hash_dig_res1 = hash_obj1.hexdigest()
    return hash_dig_res1


def hash2(passw):
    hash_obj2 = sha256(((passw)*3).encode("utf-8"))
    hash_dig_res2 = hash_obj2.hexdigest()
    return hash_dig_res2


print(hash1(password))
print(hash2(password))

password_again = input("Продублируйте пароль: ")

print(hash1(password_again))
print(hash2(password_again))

