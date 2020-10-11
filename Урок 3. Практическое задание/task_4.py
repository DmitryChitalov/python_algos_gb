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


class UrlCacher:
    def __init__(self):
        self._cache = {}
        self._salt = uuid.uuid4().bytes

    def _hashed(self, url: str):
        return hashlib.sha256(url.encode() + self._salt).hexdigest()

    def _content(self, url: str):
        with urllib.request.urlopen(url) as r:
            html = r.read()
        return html

    def _cached(self, hurl: str):
        return bool(self._cache.get(hurl))

    def _add_url(self, url: str):
        print(f'Adding {url} to cache...')
        self._cache[self._hashed(url)] = self._content(url)
        if self._cached(self._hashed(url)):
            print('Success! \n', 50 * '.')

    def process(self, urllist):
        for url in urllist:
            print(f'Processing {url}: ')
            if not self._cached(self._hashed(url)):
                print(f'{url} is not cached...')
                self._add_url(url)
            else:
                print(f'{url} is already cached!')

    def __str__(self):
        if self._cache.keys():
            res = ''
            for key in self._cache.keys():
                res += f'{key}, '
            return res
        else:
            return 'Cache is empty'


if __name__ == '__main__':

    testlist = ['http://python.org', 'http://google.com', 'http://ya.ru']
    cacher = UrlCacher()
    print(cacher)
    cacher.process(testlist)
    print(50 * '-')
    print(cacher)  # хранятся хэши и контент!
    print(50 * '-')
    cacher.process(['http://ya.ru'])  # Проверка на уже кэшированные данные

    # Можно реализовать хэширование и проверку самого содержания страницы,
    # но пока остановлюсь на этом ))
