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
    salt = 'salt'
    hash_url = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
    if cache is not None and hash_url in cache:
        return cache[hash_url]
    else:
        cache[hash_url] = url
    return url


if __name__ == '__main__':
    cache = {}
    check_cache('https://vk.com', cache)
    check_cache('https://geekbrains.ru', cache)
    check_cache('https://e.mail.ru/inbox', cache)
    check_cache('https://vk.com', cache)
    check_cache('https://geekbrains.ru', cache)
    print(cache.values())
