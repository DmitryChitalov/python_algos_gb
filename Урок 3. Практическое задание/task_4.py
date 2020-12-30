"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете усложнить задачу, реализовав ее через ООП
"""
import hashlib
from uuid import uuid4

salt = uuid4().hex
cache = {}


def add_to_cache(url):
    if url not in cache:
        cache[url] = hashlib.sha256(url.encode() + salt.encode()).hexdigest()
        print(f'url {url} добавлен в кеш')
    else:
        print(f'url {url} есть в кеше')


urls = [
    'www.yandex.ru',
    'www.yandex.ru/test',
    'www.yandex.ru/test',
    'www.yandex.ru/test',
    'www.yandex.ru/test',
    'www.yandex.ru/test1',
    'www.yandex.ru/test2',
]

for url in urls:
    add_to_cache(url)

print(cache)
