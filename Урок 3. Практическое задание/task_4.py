"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

import hashlib


def check_cache(url, cache):
    salt = 'qwerty'
    hash_url = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
    if cache is not None and hash_url in cache:
        return cache[hash_url]
    else:
        cache[hash_url] = url
    return url


if __name__ == '__main__':
    cache = {'a375bb22fc6c4ea7a8bfcb5dab369b8610d2a5b9de1f36914acb195aa471d04a': 'https://yandex.ru'}
    # cache = {}
    check_cache('https://yandex.ru', cache)
    check_cache('https://ya.ru', cache)
    check_cache('https://geekbrains.ru', cache)
    check_cache('https://e.mail.ru/inbox', cache)
    check_cache('https://vk.com', cache)
    check_cache('https://vk.com', cache)
    print(cache.items())
