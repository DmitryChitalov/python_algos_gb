"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

import os
import json
from binascii import hexlify
from hashlib import pbkdf2_hmac

user_data_file_name = 'task_4_users_urls.json'


def to_hash_url(new_url):
    obj = pbkdf2_hmac(
        hash_name='sha256',
        password=new_url[:5].encode('utf-8'),
        salt=new_url.encode('utf-8'),
        iterations=100)
    return hexlify(obj).decode('utf-8')


def check_url(check_list):
    inp_url = input('Введите url: ')
    hash_url = to_hash_url(inp_url)

    if hash_url in check_list:
        answer = input('url уже был закеширован, проверить другой url? (д/н): ').lower()
        print()
        if answer in ['д', 'l']:
            check_url(check_list)
    else:
        check_list.append(hash_url)
        answer = input('url добавлен в кеш, проверить другой url? (д/н): ').lower()
        print()
        if answer in ['д', 'l']:
            check_url(check_list)
        else:
            print('кеш страниц обновлен, всего доброго')
    return check_list


def write_data_in_file(new_data, file_name):
    with open(file_name, 'w') as f:
        json.dump(new_data, f, indent=4)


def get_data_from_json_file(file_name):
    with open(file_name, 'r') as file:
        return json.load(file)


if __name__ == '__main__':
    if os.path.isfile(user_data_file_name):
        users_data = get_data_from_json_file(user_data_file_name)
    else:
        users_data = list()

    new_urls_list = check_url(users_data)

    print('\nИтого кэши в памяти:')
    for n, cash in enumerate(new_urls_list):
        print(f'{n+1}. {cash}')
    write_data_in_file(new_urls_list, user_data_file_name)
