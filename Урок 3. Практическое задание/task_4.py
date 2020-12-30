"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
import random
import hashlib

def salt_gen(len = 10):
    return "".join(random.choice("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") for i in  range(len))



class urlCacher:
    def __init__(self):
        self.cache = {}
        self.__SALT = salt_gen(16)

    def is_empty(self):
        return self.cache == {}

    def insert_into_cache(self,url_string):
        __hash = hashlib.md5(self.__SALT.encode() + url_string.encode()).hexdigest()
        self.cache.setdefault(__hash,url_string)

    def __str__(self):
        return str(self.cache)

mycache = urlCacher()
mycache.insert_into_cache("https://test1.ru")
mycache.insert_into_cache("https://test2.ru")
mycache.insert_into_cache("https://test3.ru")
mycache.insert_into_cache("https://test3.ru/url1")
mycache.insert_into_cache("https://test3.ru/url2")
mycache.insert_into_cache("https://test1.ru")

print(mycache)