"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

a = {}

from hashlib import sha256
from uuid import uuid4

salt = uuid4().hex


def url(address):
    if a.get(address):
        print('address is in cache')
    else:
        res = sha256(address.encode() + salt.encode()).hexdigest()
        a[address] = res
        print('address added in cache')



url('https://yandex.ru/')
url('https://yandex.ru/')

print(a)
