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
kesh = {}


def check_site(url):
    if kesh.get(url):
        print('Этот адрес есть в кэше')
    else:
        hash_site = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        kesh[url] = hash_site
        print(f'Сайт {url} добавлен в кэш')


check_site('https://geekbrains.ru/lessons/94281')
check_site('https://geekbrains.ru/lessons/94281')
