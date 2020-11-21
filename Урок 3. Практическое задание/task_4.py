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

def get_page(url):
    if cache.get(url):
        print(f'Url: {url} is IN cache')
    else:
        result = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        cache[url] = result
        print(cache)

get_page('https://www.yandex.ru')
get_page('https://www.yandex.ru')
