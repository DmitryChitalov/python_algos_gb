"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""


from uuid import uuid4
import hashlib


salt = uuid4().hex.encode('utf-8')
cash_url = {}


def into_cash(url=''):
    if cash_url.get(url):
        print(f'Веб-страница {url} есть в кэше!')
    else:
        cash_url[url] = hashlib.sha256(url.encode('utf-8') + salt).hexdigest()
        print(cash_url)


into_cash('mail.ru')
into_cash('yandex.ru')
into_cash('mail.ru')
into_cash('yandex.ru')

