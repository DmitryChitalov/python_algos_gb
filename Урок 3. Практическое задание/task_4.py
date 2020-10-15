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

url_hash = {}


def hash_check(url):
    hash_obj = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
    if hash_obj not in url_hash.values():
        url_hash[url] = hash_obj


hash_check('https://geekbrains.ru')

print(url_hash)
