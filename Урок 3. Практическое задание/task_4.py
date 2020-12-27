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

dct_url = {}
salt = uuid4().hex


def check_url(url):
    if dct_url.get(url):
        return print(f'{url} in cache')
    else:
        val = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        dct_url[url] = val
        return print(f'{url} added to cache')


check_url('geekbrains.ru')
check_url('yandex.ru')
check_url('geekbrains.ru')
print(dct_url)
