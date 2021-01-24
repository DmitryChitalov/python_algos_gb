"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

import hashlib
url1 = 'https://yandex.ru'
url2 = 'https://google.com'
url_cash = []
salt = "salt"


def url_casher(url):
    return hashlib.sha256(salt.encode() + url.encode()).hexdigest()


def url_check(url):
    if url_casher(url) in url_cash:
        print(f'{url} уже в списке')
    else:
        url_cash.append(url_casher(url))
        print(f'{url} записан в кеш')


url_check(url1)
url_check(url2)
url_check(url1)
url_check(url2)
