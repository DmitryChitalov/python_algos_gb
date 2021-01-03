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
cached_url = {}


def check_url():
    url = input('Введите адрес: ')
    if cached_url.get(url):
        print('Введенный адрес имеется в кэше')
    else:
        hashed_url = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        cached_url[url] = hashed_url
        print('Адрес добавлен в кэш')


check_url()
check_url()

