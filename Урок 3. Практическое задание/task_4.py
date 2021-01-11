"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

import hashlib
from uuid import uuid4

cache = {}


def func_cache(page):
    if cache.get(page):
        print('Сайт в кэше!')
    else:
        salt = uuid4().hex
        url = hashlib.sha256(page.encode('utf-8') + salt.encode('utf-8'))
        hash_object = url.hexdigest()
        print(hash_object)
        cache[page] = hash_object
        print(cache)


func_cache('www.yandex.ru')