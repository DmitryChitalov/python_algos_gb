"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

from uuid import uuid4
from hashlib import sha256


salt = uuid4().hex
data_base = dict()


def get_page(url):
    if data_base.get(url):
        print(f'Адрес уже есть в базе.')
    else:
        data_base[url] = sha256(salt.encode() + url.encode()).hexdigest()


get_page('https://yandex.ru')
get_page('https://google.com')
get_page('https://yandex.ru')
print(data_base)
