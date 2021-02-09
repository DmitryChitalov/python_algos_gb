"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
import hashlib
import os

class UrlCacheClass:
    def __init__(self):
        self.cache = {}

    def get_cache(self, in_url):
        if self.cache.get( in_url ):
            print('Cache hit')
            res = self.cache.get( in_url )
        else:
            print('Cache miss')
            salt = os.urandom(32)
            self.cache[ in_url ] = hash( salt + in_url.encode('utf-8') )
            res = self.cache.get(in_url)
        return res

v_cache = UrlCacheClass()
v_res = v_cache.get_cache('www.google.com')
v_res = v_cache.get_cache('www.google.com')
v_res = v_cache.get_cache('www.yandex.ru')
v_res = v_cache.get_cache('www.google.com')

