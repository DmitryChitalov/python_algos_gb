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


salt = uuid4().hex
cache_with_urls = {}


def url_cache(url):
    if cache_with_urls.get(url):
        print(f'{url} уже записан в кэш')
    else:
        url_hash = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        cache_with_urls[url] = url_hash
        print(f'{url} записан в кэш - {url_hash}')


url_cache('www.yandex.ru')
url_cache('www.yandex.ru')
url_cache('www.mail.ru')

print(cache_with_urls)
