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
from functools import wraps


class CachingUrl:
    def __init__(self, url):
        self.url = url

    def _memorize(func):
        """
        Декоратор, который проверяет есть ли страница в кэш, если нет, то кэширует хэш страницы.
        """
        @wraps(func)
        def wrap(self, memory={}):
            r = memory.get(self.url)
            if r is None:
                r = func(self)
                memory[self.url] = r
                print(f'Страница внесена в кэш!')
            else:
                print(f'Достали страницу из кэша!')
            return r
        return wrap

    @_memorize
    def caching(self):
        result = hashlib.sha256(self.url.encode('utf-8') + uuid4().hex.encode('utf-8')).hexdigest()
        return result


url_1 = CachingUrl('http://stackoverflow.com')
url_1.caching()

url_2 = CachingUrl('http://facebook.com')
url_2.caching()

url_3 = CachingUrl('http://stackoverflow.com')
url_3.caching()

url_4 = CachingUrl('http://twitter.com')
url_4.caching()

url_5 = CachingUrl('http://facebook.com')
url_5.caching()

