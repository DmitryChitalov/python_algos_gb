"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

#Решение снова взято из лекций

from uuid import uuid4
import hashlib

salt = uuid4().hex      #очень удобная соль

some_cache = {}

def get_page(url):
    if some_cache.get(url):
        print(f'Данный адрес: {url} присутствует в кэше')
    else:
        res = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        some_cache[url] = res
        print(some_cache)

get_page('https://geekbrains.ru/')
get_page('https://geekbrains.ru/')
get_page('https://yandex.ru/')
get_page('https://yandex.ru/')
