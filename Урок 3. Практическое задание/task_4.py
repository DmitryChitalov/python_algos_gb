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


class Cache:
    def __init__(self):
        self.cache_obj = {}

    def get_page(self, url):
        salt = uuid4().hex
        if self.cache_obj.get(url):
            return f'Данный адрес: {url} присутствует в кэше'
        else:
            res = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
            self.cache_obj[url] = res
            return self.cache_obj


c = Cache()
c.get_page('https://geekbrains.ru/')
print(c.get_page('https://geekbrains.ru/'))
