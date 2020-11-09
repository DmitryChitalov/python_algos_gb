"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
from uuid import uuid4
import hashlib
import time
from functools import wraps


# def stopwatch(func):
#     @wraps(func)
#     def wrapper(*args):
#         start_val = time.time()
#         result = func(*args)
#         end_val = time.time()
#         print(f'Операция заняла: {end_val - start_val:.10f} сек')
#         return result
#     return wrapper
#
#
# def memorize(func):
#     @stopwatch
#     def g(url, memory={}):
#         r = memory.get(url)
#         if r is None:
#             r = func(url)
#             memory[url] = r
#             # print(memory)
#         return r
#     return g
#
#
# @memorize
# def hash_url(url):
#     salt = uuid4().hex
#     res = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
#     return res
#
#
# url = 'http://stackoverflow.com'
# hash_url(url)
#
# url = 'http://facebook.com'
# hash_url(url)
#
# url = 'http://python.org'
# hash_url(url)
#
# url = 'http://instagram.com'
# hash_url(url)
#
# url = 'http://twitter.com'
# hash_url(url)
#
# url = 'http://stackoverflow.com'
# hash_url(url)


class CachingUrl:
    def __init__(self):
        self.url = []
        self.salt = uuid4().hex
        self.result = []

    def _memorize(func):
        def wrap(self, memory={}):
            r = memory.get(self.url)
            if r is None:
                r = func(self.url)
                memory[self.url] = r
            return r
        return wrap

    @_memorize
    def hash_url(self, url):
        self.result = hashlib.sha256(self.salt.encode('utf-8') + url.encode('utf-8')).hexdigest()
        print(type(self.result))
        return self.result


url_1 = CachingUrl()
url_1.hash_url('http://stackoverflow.com')

url_2 = CachingUrl()
url_2.hash_url('http://facebook.com')

url_1 = CachingUrl()
url_1.hash_url('http://stackoverflow.com')
