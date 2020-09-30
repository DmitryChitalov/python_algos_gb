"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
import hashlib
from uuid import uuid4

salt = uuid4().hex
cache_list = {}


def cache_page(url):
    if cache_list.get(url):
        print(f'Данный адрес: {url} уже присутствует в кэше')
    else:
        res = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        cache_list[url] = res
        print(f'Адрес: {url} был добавлен в кэш')


cache_page('https://geekbrains.ru/')
cache_page('https://geekbrains.ru/')
cache_page('https://www.google.ru/')
cache_page('https://www.google.ru')
