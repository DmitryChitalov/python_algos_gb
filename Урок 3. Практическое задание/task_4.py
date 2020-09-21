"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

import urllib.request
import hashlib
from uuid import uuid4


class OpenAdd:
    def __init__(self):
        self.bd = {}
        self.salt = uuid4().hex

    def open(self, url):
        key = hashlib.sha256(self.salt.encode() + url.encode()).hexdigest()
        if key in self.bd.keys():
            return self.bd[key].read()
        else:
            doc = urllib.request.urlopen(url)
            self.bd[key] = doc
            return self.bd[key].read()


url1 = "https://docs.python.org/3/library/urllib.request.html"
url2 = 'https://docs.python.org/3/contents.html'
url3 = 'https://docs.python.org/3/whatsnew/3.8.html'
url4 = 'https://docs.python.org/3/whatsnew/3.8.html#new-features'
sait = OpenAdd()
print(sait.open(url1))
print(sait.open(url2))
print(sait.open(url3))
print(sait.open(url4))
print(sait.open(url1))
