"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

import hashlib


class HashedPage:
    def __init__(self):
        self.page_urls = dict()

    def add_url(self, hashed_result, url):
        self.page_urls[hashed_result] = url

    def check_url(self, url):
        if self.page_urls.get(url):
            return True
        else:
            return False

    def get_collect(self):
        print(self.page_urls)


my_links = HashedPage()

url_1 = 'https://github.com/'
url_2 = 'https://geekbrains.ru/'


def pages_hashing(_url):
    salt = _url[7:11]
    hashed_result = hashlib.sha256(salt.encode('utf-8') + _url.encode('utf-8')).hexdigest()
    checker = my_links.check_url(hashed_result)
    if not checker:
        my_links.add_url(hashed_result, _url)
        print('Страницы не было, страница внесена')
    else:
        print('Страница уже есть в кэше')


pages_hashing(url_1)
pages_hashing(url_1)
pages_hashing(url_2)
