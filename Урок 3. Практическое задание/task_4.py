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
import requests

salt = uuid4().hex
url_cache = {}


def update_cache(url):
    if url_cache.get(url):
        print('Этот url есть в кэше.')
        return
    try:
        response = requests.get(url)
        if response:
            page_hash = hashlib.sha256(salt.encode() + response.text.encode()).hexdigest()
            url_cache.update({url: page_hash})
            print('Страница добавлена в кэш.')
        else:
            print('Что-то пошло не так')
    except OSError:
        print('Неверный url')


update_cache('https://translate.google.com')
update_cache('https://geekbrains.ru/')
print(url_cache)
while True:
    ans = input('Введите url (или 0 для выхода):')
    if ans == '0':
        break
    update_cache(ans)
