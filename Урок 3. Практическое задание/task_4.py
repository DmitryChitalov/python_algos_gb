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

def url_checker(url, url_cache, salt):
    url_hash = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
    none_checker = url_cache.get(url_hash)
    if none_checker is None:
        url_cache[url_hash] = url
        user_url = input("Введите url. Если хотите завершить программу, введите 0. Если хотите увидеть словарь, нажмите 1: ")
        if user_url == "0":
            print("Завершаем.")
        elif user_url == "1":
            print(url_cache)
        else:
            url_checker(user_url, url_cache, salt)
    else:
        print("Такой url уже есть.")
        user_url = input("Введите url. Если хотите завершить программу, введите 0. Если хотите увидеть словарь, нажмите 1: ")
        if user_url == "0":
            print("Завершаем.")
        elif user_url == "1":
            print(url_cache)
        else:
            url_checker(user_url, url_cache, salt)


salt = uuid4().hex
user_url = input("Введите url: ")
url_cache = {}
url_checker(user_url, url_cache, salt)