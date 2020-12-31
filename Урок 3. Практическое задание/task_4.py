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
cache = {}

def task_4(url):
    if cache.get(url):
        print('Адрес есть в кеше!')
    else:
        result = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        cache[url] = result # добавляем в кеш
        print(cache)

task_4('papapa')
task_4('papapa')