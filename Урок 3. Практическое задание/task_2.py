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


def passwd_checker():
    first_input = input('пожалуйста введите пароль: ')
    second_input = input('пожалуйста повторите ввод пароля: ')
    salt = 'two big spoons of salt'

    pwd_hash_first = pbkdf2_hmac(hash_name='sha256',
                                 password=first_input.encode(),
                                 salt=salt.encode(),
                                 iterations=1000)

    pwd_hash_second = pbkdf2_hmac(hash_name='sha256',
                                  password=second_input.encode(),
                                  salt=salt.encode(),
                                  iterations=1000)

    if pwd_hash_first == pwd_hash_second:
        print('Пароли совпадают')
        print(f'хэш паролей: {pwd_hash_first}')
    else:
        print('Пароли отличаются')
        print(f'хэш первого пароля {pwd_hash_first}'
              '\n'
              f'хэш второго пароля {pwd_hash_second}'
              )


passwd_checker()
