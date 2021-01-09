import hashlib
from uuid import uuid4
import requests
"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

cache = dict()
salt = uuid4().hex      # генерируем соль


def get_url(url):
    if cache.get(url):                              # если страница уже имеется в кеше, то возвращается ее хэш
        print('Страница была загружена из кэша.')
        return cache[url]
    else:
        print(f'Подождите. Страница прогружается.')
        data = get_data_from_server(url)                # если нет, то url страницы хэшируется
        cache[url] = data                               # и заносится в кэш
        return data


def get_data_from_server(url):
    data_hash = hashlib.sha1(salt.encode() + url.encode()).hexdigest()      # хешируем адрес страницы
    return data_hash


get_url('https://mail.ru/')             # загружаем новые страницы
get_url('https://love.mail.ru/ru')
get_url('https://ok.ru/')

get_url('https://mail.ru/')             # загружаем уже имеющуюся в кеше страницу

print(cache)