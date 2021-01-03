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
cache = {}


def check_page(url):
    if cache.get(url):
        print(f'Данный адрес есть в кэше')
    else:
        res = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        cache[url] = res
        print(cache)


check_page('https://news.ru/')
check_page('https://books.ru/')
check_page('https://books.ru/')