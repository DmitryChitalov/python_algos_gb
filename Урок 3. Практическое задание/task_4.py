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

the_cash = []
salt = uuid4().hex

def make_some_cash(url):
    cash_the_page = hashlib.sha512(salt.encode()+url.encode()).hexdigest() + ':' + salt
    if cash_the_page in the_cash:
        print(f'Page you enter - {url} - has been added to the cash already!')
    elif cash_the_page not in the_cash:
        the_cash.append(cash_the_page)
        print(f'Page {url} added to the cash!')


make_some_cash('https://google.com')
make_some_cash('https://habr.com/ru/')
make_some_cash('https://habr.com/ru/')
make_some_cash('https://pikabu.ru/')
make_some_cash('https://pikabu.ru/')

print(the_cash)