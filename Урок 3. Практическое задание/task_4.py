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

salt = uuid4().hex

cash_dict = {}


def cash_func(url):
    if cash_dict.get(url):
        return f'{url} присутствует в кэше'
    else:
        hash = hashlib.sha256(salt.encode('utf-8') +
                              url.encode('utf-8')).hexdigest() + ':' + salt
        cash_dict[url] = hash
        return f'{url} добавлен в кэш'


print(cash_func('https://mail.ru'))
print(cash_func('https://www.google.ru/'))
print(cash_func('https://mail.ru'))
print(cash_func('https://github.com/'))
print(cash_dict)