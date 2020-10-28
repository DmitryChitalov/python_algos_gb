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

import hashlib
from string import ascii_letters
from random import choice

users = {}  # используем словарь для хранения данных для аутентификации пользователей
"""
Приложение запрашивает логин, если пользователя с таким логином нет - предлагает создать учетку, затем
предлагает авторизироваться. В словаре храним в качестве ключа ник, в качестве значения кортеж с хешем
соленого пароля и отдельно соль
"""


def encode_password(password, salt):
    """Хеширует и солит пароль"""
    auth_data = hashlib.sha256(password.encode() + salt.encode()).hexdigest()
    return auth_data


def is_user_registered(nick_name):
    """Проверка наличия регистрации пользователя в системе"""
    return nick_name in users.keys()


def register_user(nick_name, password):
    """Функция регистрирует нового пользователя в системе"""
    salt = nick_name + ''.join(
        choice(ascii_letters) for _ in range(10))  # соль = уникальный логин + усложняем комбинацией букв
    auth_data = encode_password(password, salt)  # хешируем пароль с солью
    users[nick_name] = (auth_data, salt)  # сохраняем отдельно хешированный соленый пароль и соль в кортеже


def auth_user(nick_name, password):
    """Аутентифицирует пользователя"""
    auth_data = encode_password(password, users[nick_name][1])
    if nick_name in users.keys() and users[nick_name][0] == auth_data:
        return True
    return False


def app():
    """Точка входа в приложение"""
    while True:
        login = input('Ввведите логин или 0 для выхода: ')
        if login == '0':
            print('Сеанс завершен')
            exit()
        password = input('Введите пароль: ')
        if not is_user_registered(login):
            register_user(login, password)  # проверяем, зарегестрирован ли пользователь с таким логином
            print(f'Учетная запись для пользователя с ником {login} успешно создана. Авторизируйтесь')
        else:
            if auth_user(login, password):
                print('-' * 100, 'Вход выполнен', sep='\n')
                print(f'Для данного пользователя в  БД хранится хеш: {users[login][0]} и соль: {users[login][1]}')
                break
            else:
                print('Вы ввели неверный пароль')


if __name__ == '__main__':
    app()
