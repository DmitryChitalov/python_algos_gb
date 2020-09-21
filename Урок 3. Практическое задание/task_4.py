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


def get_page(url, user):
    salt = user.encode()
    hash_url = hashlib.sha256(url.encode() + salt).hexdigest()
    if cache.get(url):
        return cache
    else:
        cache[url] = hash_url
        return cache


print(get_page('www.yandex.ru', 'Ivan'))
print(get_page('www.yandex.ru', 'Ivan'))
print(get_page('www.qwe.ru', 'Asdf'))
print()
print(cache)
