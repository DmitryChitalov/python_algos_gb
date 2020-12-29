"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""


from uuid import uuid4
import hashlib


def get_page(our_url):
    if cache.get(our_url):
        print(f'{our_url} in cache')
    else:
        cache[our_url] = hashlib.sha256(salt.encode() + our_url.encode()).hexdigest()
        print(cache)


salt = uuid4().hex
cache = {}

get_page('https://yandex.ru/')
get_page('https://yandex.ru/')