"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете усложнить задачу, реализовав ее через ООП
"""

from uuid import uuid4
import hashlib

salt = uuid4().hex
print(salt)
cache_mem_table = {}


def url_check(url):
    if cache_mem_table.get(url):
        print(f'This page is in cache table!')
    else:
        res = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        cache_mem_table[url] = res
        print(cache_mem_table)


url_check('https://yandex.ru/')
url_check('https://yandex.ru/')


