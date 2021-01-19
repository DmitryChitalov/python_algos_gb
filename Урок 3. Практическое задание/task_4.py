"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

import hashlib
import json

def cache_url(url):

    salt = str(url[1:-2])
    hash_url = hashlib.sha256(salt.encode('utf-8') + url.encode('utf-8')).hexdigest()

    with open('cache_table.json', 'r', encoding='utf-8') as r_file:
        data = json.load(r_file)

    if data.get(hash_url):
        print(f'Url уже существует в таблице')
        return
    else:
        data.update({hash_url: url})
        with open('cache_table.json', 'w', encoding='utf-8') as w_file:
            json.dump(data, w_file)
        print(f'Url внесен в таблицу')
        return


# проверка

cache_url('https://yandex.ru/')
cache_url('https://google.ru/')
cache_url('https://geekbrains.ru/')
cache_url('https://mail.ru/')






