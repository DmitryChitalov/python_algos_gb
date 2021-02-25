"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации
"""
from uuid import uuid4
import hashlib

salt = uuid4().hex  # -> 952604f24d9f4cd0b515a39c73657027
cache_obj = {}


def add_page(url):
    if cache_obj.get(url):
        print(f'Address {url} already in cache')
    else:
        res = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        cache_obj[url] = res
        print(cache_obj)


add_page('https://geekbrains.ru/')
add_page('www.amdocs.com')
add_page('https://geSekbrains.ru/')
