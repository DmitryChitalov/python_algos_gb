"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""


import hashlib as has
import uuid as uu


salt = uu.uuid4().hex
cash_dict = {}


def url_cash_dict(url):
    if cash_dict.get(url):
        return f'{url} уже кеширован.'
    else:
        h = has.sha512(salt.encode() + url.encode()).hexdigest()
        cash_dict[url] = h
        return f'{url} кеширован'


print(url_cash_dict('https://geekbrains.ru/'))
print(url_cash_dict('https://geekbrains.ru/'))
print(url_cash_dict('https://habr.com/ru/'))
print(url_cash_dict('https://habr.com/ru/'))

for key in cash_dict:
    print(f'{key}: {cash_dict[key]}')

