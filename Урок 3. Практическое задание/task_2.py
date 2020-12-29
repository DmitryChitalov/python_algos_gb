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

salt = uuid4().hex
print(salt)


def authentification():
    attempt_passwd = input('Please, input password: ')
    res = hashlib.sha256(salt.encode() + attempt_passwd.encode()).hexdigest()
    print(f'String {res} stores in database')
    passwd_verification = input('Please, input password once again for verification: ')
    if passwd_verification == attempt_passwd:
        if hashlib.sha256(salt.encode() + passwd_verification.encode()).hexdigest() == res:
            return print('Welcome, your data is correct!')
    else:
        return print('Your data is not correct!')


authentification()