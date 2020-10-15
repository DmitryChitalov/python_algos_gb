"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
import uuid
import hashlib
import urllib.request

class WebCacher:

    def __init__(self):
        self._cache = {}
        self._salt = uuid.uuid4().bytes

    def _hash(self, url: str):
        return hashlib.sha256(url.encode() + self._salt).hexdigest()

    def _content(self, url: str):
        with urllib.request.urlopen(url) as c:
            if c.getcode() == 200:
                return c.read()
            else:
                print(f"Can't get content on link {url}.")

    def cached(self, url: str):
        return bool(self._cache.get(self._hash(url)))

    def add_to_cash(self, url: str):
        if self._content(url):
            self._cache[self._hash(url)] = self._content(url)
        if not self.cached(url):
            print('Cashing was failed.')

if __name__ == '__main__':
    url_list = ['https://geekbrains.ru', 'https://www.google.com/']
    casher = WebCacher()
    casher.add_to_cash(url_list[0])
    for url in url_list:
        print(f'{url} is in cache.') if casher.cached(url) else \
            print(f'{url} is not in cache.')