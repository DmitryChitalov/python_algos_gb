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


class Cache:

    def __init__(self):
        self._cache_set = set()
        self._salt = uuid4().hex.encode('utf-8')

    def check_cache(self, url):
        if hashlib.md5(url.encode('utf-8') + self._salt).hexdigest() in self._cache_set:
            return True
        else:
            return False

    def add_cache(self, url: str):
        if not self.check_cache(url):
            self._cache_set.add(hashlib.md5(url.encode('utf-8') + self._salt).hexdigest())
            print(f'Копия страницы {url} помещена в кэш')
        else:
            print(f'Копия страницы {url} уже содержится в кэше')


my_cache = Cache()

while True:
    my_url = input('Введите URL или \'exit\' для выхода: ')
    if my_url != 'exit':
        my_cache.add_cache(my_url)
    else:
        break
