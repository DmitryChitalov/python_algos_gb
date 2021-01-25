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
import random
import string
import json


def save_password():
    password = input('Add password: ')
    salt = generate_salt(16)
    make_hash = hashlib.sha3_256((password + salt).encode('utf-8'))
    save_data = {
        'salt': salt,
        'password': make_hash.hexdigest()
    }
    create_conf(save_data)
    return 'Данные сохранены'


def create_conf(user_data):
    with open('password.json', 'w', encoding="utf-8") as file_json:
        json.dump(user_data, file_json)


def generate_salt(length):
    '''
    Функция генерации соли
    :param length: не меньше 16 символов для большей безопасности
    :return: Возвращается строка mix
    '''
    letters_and_digits = string.ascii_letters + string.digits
    rand_string = ''.join(random.sample(letters_and_digits, length))
    return rand_string


def check_password():
    with open("password.json", "r") as read_conf:
        user_data = json.load(read_conf)

    print('Введите ранее установленный пароль!')
    password = input('Password: ')
    salt = user_data['salt']
    make_hash = hashlib.sha3_256((password + salt).encode('utf-8'))
    if make_hash.hexdigest() != user_data['password']:
        return 'Deny'
    else:
        return 'Ok'


def program_exit():
    return 'Вы завершили работу'


try:
    print('Введите 1 для создания пароля или 2 для сверки пароля. 0 - выход')
    user_inp = input('Commands: ')
    data = {
        '0': program_exit,
        '1': save_password,
        '2': check_password
    }
    print(data[user_inp]())
except KeyError:
    print('Error, this is not command')
