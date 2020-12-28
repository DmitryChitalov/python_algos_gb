"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

from hashlib import sha256

SALT = b'salt'
storage = dict()


def cache_www(url):
    if storage.get(url):
        print(f'Страница с адресом "{url}" уже есть в кэше')
    else:
        storage[url] = sha256(SALT + url.encode()).hexdigest()
        print(storage)


cache_www('google.com')
cache_www('vk.com')
cache_www('geekbrains.ru')
cache_www('google.ru')
cache_www('google.ru')
