"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

from hashlib import sha256
from uuid import uuid4

cache = {}


def my_func(url):
    if cache.get(url):
        print('Кэш уже есть')
    else:
        salt = uuid4().hex
        cache[url] = sha256(url.encode() + salt.encode()).hexdigest()
        print('Занесен в кэш url: {} - {}'.format(url, cache[url]))


my_func('http://ya.ru')
my_func('http://google.com')
my_func('http://yandex.ru')
my_func('http://ya.ru')
my_func('http://mail.ru')
