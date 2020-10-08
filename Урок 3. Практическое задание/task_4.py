"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

########################################################################################################################

import hashlib

cache = {}


def cache_memory():
    salt = hashlib.sha256(b'Hakuna_Matata').hexdigest()
    link = input('url - адрес: ')
    hash_link = hashlib.sha256(salt.encode() + link.encode()).hexdigest() + '?' + salt
    if link not in cache:
        cache[hash_link] = hashlib.sha256(salt.encode()).hexdigest()
    return cache


print(cache_memory())

########################################################################################################################

cache_two = {}


class CacheMemory:

    def __init__(self, link):
        self.salt = hashlib.sha256(b'Hakuna_Matata').hexdigest()
        self.link = link

    def hash(self):
        self.link = hashlib.sha256(self.salt.encode() + self.link.encode()).hexdigest() + '?' + self.salt

    def add_cache(self):
        if self.link not in cache_two:
            cache_two[self.link] = hashlib.sha256(self.salt.encode()).hexdigest()
        return cache_two


def cache_memory():
    cm = CacheMemory(input('link: '))
    cm.hash()
    cm.add_cache()
    print(cm.add_cache())


cache_memory()

