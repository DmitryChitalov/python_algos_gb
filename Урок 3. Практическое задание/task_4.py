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


class Cache:
    def __init__(self):
        self._salt = uuid4().hex
        self._pages = {}

    def _url_key(self, url):
        return hashlib.sha256(url.encode() + self._salt.encode()).hexdigest()

    def get_page(self, url):
        return self._pages.setdefault(self._url_key(url), url)


if __name__ == '__main__':

    local_cache = Cache()
    local_cache.get_page('https://geekbrains.ru')
    local_cache.get_page('https://geekbrains.ru')
    local_cache.get_page('https://refactoring.guru')
    local_cache.get_page('https://refactoring.guru')

    # print(local_cache._pages)
