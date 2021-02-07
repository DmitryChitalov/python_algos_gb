"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
from hashlib import sha256

class url_cache:
    _cached_urls = {}
    _salt = 'saltener'
    def get_url_cached(self,url):
        if self._cached_urls.get(url):
            print(f"Страница {url} в кеше")
        else:
            res = sha256(url.encode()+self._salt.encode()).hexdigest()
            self._cached_urls[url] = res

a = url_cache()

a.get_url_cached("http://ya.ru")
a.get_url_cached("http://b.ru")
a.get_url_cached("http://c.ru")
a.get_url_cached("http://b.ru")
a.get_url_cached("http://ya.ru")

