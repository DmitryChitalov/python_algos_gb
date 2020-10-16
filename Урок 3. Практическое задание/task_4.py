"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете усложнить задачу, реализовав ее через ООП
"""

from hashlib import sha1
from uuid import uuid4

salt = uuid4().hex
cached_pages = dict()


def cache_page(url):
    if cached_pages.get(url):
        print(f'Страница с адресом "{url}" уже есть в кэше')
    else:
        cached_pages[url] = sha1(salt.encode() + url.encode()).hexdigest()
        print(cached_pages)


cache_page('yandex.ru')
cache_page('google.com')
cache_page('yandex.ru')
