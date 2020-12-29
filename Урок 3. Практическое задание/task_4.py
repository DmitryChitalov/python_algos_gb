"""
Задача 4.
Реализуйте скрипт "Кеширование веб-страниц"
Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
from uuid import uuid4
from hashlib import sha256

salt = uuid4().hex
set_cache = dict()


def is_cache(url):
    if set_cache.get(url):
        print(f'В кэше уже содержится адрес {url}')
    else:
        set_cache[url] = sha256(salt.encode() + url.encode()).hexdigest()


is_cache('https://yandex.ru/')
is_cache('https://www.google.ru/')
is_cache('https://yandex.ru/')
