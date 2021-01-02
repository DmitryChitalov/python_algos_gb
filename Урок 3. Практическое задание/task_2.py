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


def show_hash(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(f'{args[0]} - {res}')
        return res
    return wrapper


@show_hash
def hash_password(pwd, slt):
    return hashlib.sha256(pwd.encode() + slt.encode()).hexdigest()


def check_password(new_pwd, slt, old_pwd_hash):
    return hash_password(new_pwd, slt) == old_pwd_hash


if __name__ == '__main__':
    salt = uuid4().hex
    password = input('Введите пароль: ')
    hashed_password = hash_password(password, salt)
    password = input('Повторите пароль: ')
    if check_password(password, salt, hashed_password):
        print('Пароль верный')
    else:
        print('Пароль не верный')
