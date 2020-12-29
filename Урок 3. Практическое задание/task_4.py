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

web_pages = {}
salt = uuid4().hex


def check_or_cache(url):
    if url in web_pages:
        print("Страница есть а кэше.")
    else:
        web_pages[url] = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        print('Страница добавлена в кэш.')


check_or_cache('http://www.yandex.ru')
check_or_cache('http://www.yandex.ru')
