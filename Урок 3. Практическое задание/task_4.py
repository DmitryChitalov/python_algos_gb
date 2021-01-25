"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

import hashlib
from uuid import uuid4


def page_url(url):
    if url_hash.get(url):
        print(f'{url} уже присутствует в кэше')
    else:
        res = hashlib.sha1(salt.encode('utf-8') + url.encode('utf-8')).hexdigest()
        url_hash[url] = res
        print(url_hash)


salt = uuid4().hex  
url_hash = dict()


page_url('youtube.com')
page_url('youtube.com')
page_url('yandex.ru')
page_url('yandex.ru')
