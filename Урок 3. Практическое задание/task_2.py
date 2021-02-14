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


class User:

    def __init__(self):
        self._username = input('Введите имя пользователя: ')
        while True:
            passwd = input('Введите пароль: ')
            self._passwd_hash = hexlify(pbkdf2_hmac(hash_name='sha256',
                                                    password=passwd.encode(),
                                                    salt=self._username.encode(),
                                                    iterations=100000))
            print(f'Хэш-строка для введенного пароля: {self._passwd_hash}')
            passwd = input('Введите пароль повторно: ')
            passwd_check = hexlify(pbkdf2_hmac(hash_name='sha256',
                                               password=passwd.encode(),
                                               salt=self._username.encode(),
                                               iterations=100000))
            if passwd_check == self._passwd_hash:
                print('Учетная запись успешно создана! Вы можете зайти на ресурс, используя введенные данные')
                break
            else:
                print('Пароли не совпадают! Попробуйте указать пароль еще раз.')

    def authorize(self):
        username_input = input('Введите имя пользователя: ')
        passwd_input = input('Введите пароль: ')
        passwd_check = hexlify(pbkdf2_hmac(hash_name='sha256',
                                           password=passwd_input.encode(),
                                           salt=username_input.encode(),
                                           iterations=100000))
        if passwd_check == self._passwd_hash:
            print(f'Добро пожаловать на ресурс, {self._username}!')
        else:
            print('Неверное имя пользователя или пароль!')


new_user = User()
new_user.authorize()
