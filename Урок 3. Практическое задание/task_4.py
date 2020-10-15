"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

import hashlib

salt = '123'
url_cache = {}


def page(url):
    if url_cache.get(url):
        print(f'Данная url-сылка:{url}, уже пристусвует в кэше')
    else:
        new_cache = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        url_cache[url] = new_cache
        print(url_cache)