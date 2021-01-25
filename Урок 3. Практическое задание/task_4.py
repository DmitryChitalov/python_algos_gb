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

url = ''
url_cash = {}

salt = uuid4().hex

hash_obj = hashlib.sha256(salt.encode() + url.encode()).hexdigest()

def url_check(url):
    if url not in url_cash:
        url_cash[url] = hash_obj

    return url, hash_obj

print(url_check('https://ozon.ru'))
print(url_check('https://yandex.ru'))
