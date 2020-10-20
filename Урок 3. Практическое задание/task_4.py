"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
import hashlib

cache = {}


def cache_func(url, user):
    hash_url = hashlib.sha256(url.encode() + user.encode()).hexdigest()
    if not cache.get(url):
        cache[url] = hash_url
    return cache


print(cache_func('www.avito.ru', 'Марина'))
print(cache_func('www.yandex.ru', 'Вася'))
print(cache_func('www.google.com', 'Anna'))
print(cache_func('www.yandex.ru', 'Вася'))
print(cache)