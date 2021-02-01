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

import os
import json
from binascii import hexlify
from hashlib import pbkdf2_hmac

user_data_file_name = 'task_2_users_login_password.json'


def hash_password(user_name, user_password):
    obj = pbkdf2_hmac(
        hash_name='sha256',
        password=user_password.encode('utf-8'),
        salt=user_name.encode('utf-8'),
        iterations=100000)
    return hexlify(obj)


def write_data_in_file(new_data, file_name):
    with open(file_name, 'w') as f:
        json.dump(new_data, f, indent=4)


def get_data_from_json_file(file_name):
    with open(file_name, 'r') as file:
        return json.load(file)


def main():
    login = input('Введите логин: ')

    if os.path.isfile(user_data_file_name):
        users_data = get_data_from_json_file(user_data_file_name)
    else:
        users_data = dict()

    if login in users_data:
        user_password = input('Введите пароль: ')
        user_password_in_hash = hash_password(login, user_password).decode('utf-8')

        while user_password_in_hash != users_data[login] and user_password_in_hash != '0':
            user_password_in_hash = input('Пароль введен неверно, попробуйте ещё раз (0 для выхода): ')
            if user_password_in_hash == '0':
                print('Всего доброго')

        if user_password_in_hash == users_data[login]:
            print(f'В БД хранится строка для вашего пароля:\n{users_data[login]}')
            print('Добро пожаловать!')

    else:
        user_password = input('Такого пользователя не существует, для добавления введите пароль: ')
        user_password_in_hash = hash_password(login, user_password).decode('utf-8')
        users_data[login] = user_password_in_hash
        write_data_in_file(users_data, user_data_file_name)


if __name__ == '__main__':
    main()
