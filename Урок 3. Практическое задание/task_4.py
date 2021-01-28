"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

# my method
import hashlib
from hashlib import sha256
from uuid import uuid4


class hex_url():
    def __init__(self):
        self.salt_url = {}
        self.salt = uuid4().hex

    def input_url(self):
        url = input('Enter URL: ')
        return self.validate_u_s(url)

    def validate_u_s(self, url):
        if self.salt_url.get(url) is None:
            print('We have not cache yet')
            hexurl = sha256(self.salt.encode() + url.encode('utf-8')).hexdigest()
            self.salt_url.update({url: hexurl})
            print(f'Record complete: {self.salt_url.get(url)}')
        else:
            print(f'Record already exist: {self.salt_url.get(url)}')
        return self.input_url()


hu = hex_url()
hu.input_url()


# GB Method
salt = uuid4().hex
cache_obj = {}


def get_page(url):
    if cache_obj.get(url):
        print(f'Address {url} is in cache.')
    else:
        res = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        cache_obj[url] = res
        print(cache_obj)


get_page('https://geekbrains.ru/')
get_page('https://geekbrains.ru/')
