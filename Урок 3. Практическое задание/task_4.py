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
page_lib = {}


def get_page(url):
    if page_lib.get(url):
        print(f'Адрес {url} уже добавлен в библиотеку.')
    else:
        hex_result = hashlib.sha3_256(url.encode() + salt.encode()).hexdigest()
        page_lib[url] = hex_result
        print(page_lib)


get_page(r'https://yandex.ru/maps')
get_page(r'https://market.yandex.ru')
get_page(r'https://yandex.ru/news/')
get_page(r'https://yandex.ru/maps')