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


def add_hash(url):
    if url not in hash_list:
        hash_obj = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        hash_list[url] = hash_obj
    print(hash_list)


salt = uuid4().hex
hash_list = {}
add_hash('https://mail.ru')
add_hash('https://yandex.ru')
add_hash('https://google.ru')
add_hash('https://mail.ru')
