"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
from uuid import uuid4
from hashlib import md5


obj = {}

def check_page(url: str):
    if obj.get(url):
        print('{} уже присутствует в кэше'.format(url))
    else:
        salt = url[::-1] + uuid4().hex
        obj[url] = md5(salt.encode() + url.encode()).hexdigest()
        print(obj)

check_page('http://yandex.ru')
check_page('http://beloved-wed.ru')
check_page('http://yandex.ru')