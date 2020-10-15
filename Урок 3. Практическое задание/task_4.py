"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете усложнить задачу, реализовав ее через ООП
"""

import urllib.request
import hashlib
from uuid import uuid4


class WebPageCache:
    def __init__(self):
        self.WebPageCacheBD = {}
        self.salt = uuid4().hex

    def open_url(self, url):
        key = hashlib.sha256(self.salt.encode() + url.encode()).hexdigest()
        if key in self.WebPageCacheBD.keys():
            print('Данные взяты из кэша.')
            # print(self.WebPageCacheBD)
            # print(self.WebPageCacheBD[key].read())
            return self.WebPageCacheBD.get(key)
        else:
            web_page_data = urllib.request.urlopen(url)
            self.WebPageCacheBD[key] = web_page_data
            print('Данные взяты из сети интернет.')
            # print(self.WebPageCacheBD)
            # print(self.WebPageCacheBD[key].read())
            return web_page_data


url1 = 'https://yandex.ru/'
url2 = 'https://www.google.com/'
web_page = WebPageCache()

print(web_page.open_url(url1) == web_page.open_url(url1))
print(web_page.open_url(url2) == web_page.open_url(url2))
