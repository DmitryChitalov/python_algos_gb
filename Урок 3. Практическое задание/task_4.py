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
url_store = {}


def cash_webpages(url):
    res = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
    if len(url_store) == 0:
        url_store.update({url: res})
        return "Добавлен первый адрес."
    else:
        for items in url_store.values():
            if items == res:
                return "Адрес уже существует!"
            else:
                url_store.update({url: res})
                return "Новый адрес добавлен!"


print(cash_webpages('https://geekbrains.ru'))
print(cash_webpages('https://geekbrains.ru'))
print(cash_webpages('https://www.codecademy.com'))
print(url_store)
