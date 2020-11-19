"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
# git
import hashlib
from uuid import uuid4

my_cash = set()
salt = uuid4().hex


def cashing(url):
    page_cashing = hashlib.sha256(salt.encode()+url.encode()).hexdigest()
    if page_cashing in my_cash:
        print(f'Page{url} is already in cash')
    elif page_cashing not in my_cash:
        my_cash.add(page_cashing)
        print(f'Page{url}  added into cash')


cashing('https://spb.hh.ru/vacancy')
cashing('https://stopgame.ru')
cashing('https://www.artlebedev.ru/typograf/')
cashing('https://pythonworld.ru')
cashing('https://pythonworld.ru')
