"""
Задание 1.
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

salt = uuid4().hex


def hash_passwd(passwd):
    return hashlib.sha256(salt.encode() + passwd.encode()).hexdigest()


def check_hash_passwd(hash_passwd, check_hash):
    return hash_passwd == check_hash


hash_pass = hash_passwd(input('Введите пароль: '))
print(f'Полученный хеш - {hash_pass}')
check_hash = hash_passwd(input('Введите пароль еще раз: '))

print('Проверка пройдена!') if check_hash_passwd(hash_pass, check_hash) else print('Пароль не верный!')
