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
cach_object = {}

def get_page(url):
    if cach_object.get(url):
        print(f'Адрес {url} есть в кэше')
    else:
        res = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        cach_object[url] = res
        print(cach_object)

get_page('yandex.ru')
get_page('google.com')
get_page('mail.ru')
get_page('geekbrains.ru')
get_page('yandex.ru')