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

salt = uuid4().hex
pages_cache = set()

def page_caching(url):
    hash_url = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
    if hash_url in pages_cache:
        print(f'Адрес {url} присутствует в кэше')
    else:
        pages_cache.add(hash_url)
        print(f'Адрес {url} добавлен в кэш')

page_caching("https://ru.wikipedia.org/")   #Адрес https://ru.wikipedia.org/ добавлен в кэш
page_caching("http://duma.gov.ru/")         #Адрес http://duma.gov.ru/ добавлен в кэш
page_caching("https://ru.wikipedia.org/")   #Адрес https://ru.wikipedia.org/ присутствует в кэше