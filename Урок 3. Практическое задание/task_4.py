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

salt = uuid4().hex
kesh_tab = {}


def url(url):
    if kesh_tab.get(url):
        print("соответствующая страница ест")
    else:
        res = hashlib.sha256(salt.encode('utf-8') + url.encode('utf-8')).hexdigest()
        kesh_tab[url] = res
        print(kesh_tab)
url('https://geekbrains.ru/lessons/96319/homework')
url('https://geekbrains.ru/lessons/96319/homework')
url('https://github.com/')

