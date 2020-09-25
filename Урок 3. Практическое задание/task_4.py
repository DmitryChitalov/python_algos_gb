"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

from uuid import uuid1
import hashlib

salt = uuid1().hex
pages_lists = []


def pages_check(page):
    new_page = hashlib.sha256(salt.encode() + page.encode()).hexdigest()
    if new_page in pages_lists:
        print("Такой адрес уже существует")
    else:
        pages_lists.append(new_page)
        print('Новый адрес введен')

pages_check('https://www.zaycev.fm/rock')
pages_check('https://www.zaycev.fm/rock')
pages_check('https://www.zaycev.fm/rock')