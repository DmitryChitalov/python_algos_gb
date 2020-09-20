"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
import hashlib

salt = 'my_salt'
cache = {'b2d910abb7db92eddf88c334cf20e3ba934909a8556157cc4eed2a007f315258': 'https://geekbrains.ru',
         'fe8a56363d872a39a4bac67959fc2642a31004f59f5ba685e57755ea5bfd644f': 'https://geekbrains.ru/lessons/81319'}


def get_cache(url):
    url_hash = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
    result = cache.get(url_hash)
    if result is None:
        cache[url_hash] = url
    return url_hash


print(get_cache('https://geekbrains.ru/lessons/81319'))
print(cache)
