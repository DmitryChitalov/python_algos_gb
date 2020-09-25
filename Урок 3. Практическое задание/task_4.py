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

salt = uuid4().hex
cache = {}


def page(url):
    if cache.get(url):
        print(f"URL {url} есть в кэше!")
    else:
        result = hashlib.sha256(salt.encode() + url.encode()).hexdigest() + ":" + salt
        cache[url] = result
        print(cache)


page('https://yandex.ru')
page('https://yandex.ru')

"""

cache = []


def check_in_cache(url):
    if url in cache:
        print(f"URL {url} есть в кэше!")
    else:
        cache.append(url)
        print(cache)

check_in_cache('https://yandex.ru')
check_in_cache('https://yandex.ru')
check_in_cache('https://yandex.ru')
"""