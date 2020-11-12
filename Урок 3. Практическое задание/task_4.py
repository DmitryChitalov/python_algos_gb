"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

import uuid, hashlib

cache = {}
salt = uuid.uuid4().hex


def get_hash(obj, salt):
    res = hashlib.sha256(salt.encode() + obj.encode()).hexdigest()
    return res


def cheсk_ulr(url):
    if cache.get(url):
        print(f'Страница кэширована, хеш - {cache[url]}')
    else:
        cache[url] = get_hash(url, salt)
        print(f'Страница {url} добавлена в кэш')

cheсk_ulr("ya.ru")
cheсk_ulr('gb.ru')
cheсk_ulr('ya.ru')
print(cache)
