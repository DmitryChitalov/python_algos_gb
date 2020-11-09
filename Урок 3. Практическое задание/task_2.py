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
from hashlib import pbkdf2_hmac
from binascii import hexlify


def coding_pass(user, pwd):
    obj = pbkdf2_hmac(hash_name='sha256',
                      password=pwd.encode('utf8'),
                      salt=user.encode('utf8'),
                      iterations=100000)
    print(hexlify(obj))
    return hexlify(obj)


user_name = input('Введите логин: ')
pwd = input('Введите пароль: ')
storage = [{'login': user_name, 'passwd': coding_pass(user_name, pwd)}]

pwd_check = input('Введите пароль повторно: ')

if coding_pass(user_name, pwd_check) == storage[0].get('passwd'):
    print('Вы ввели правильный пароль!')
else:
    print('Вы ввели ошибочный пароль!')


