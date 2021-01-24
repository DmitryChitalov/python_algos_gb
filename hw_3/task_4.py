"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации
"""
import hashlib
from uuid import uuid4

memory = {}
salt = uuid4().hex


def url_cache(url):
    url_hash = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
    if memory.get(url_hash) is None:
        memory[url_hash] = url
        print("Страницы в кэше еще нет, вносим...")
    else:
        print("Страница есть в кэше, выдаем...")


url_cache("yandex.ru")
url_cache("geekbrains.ru")
url_cache("google.com")
url_cache("yandex.ru")
url_cache("geekbrains.ru")
