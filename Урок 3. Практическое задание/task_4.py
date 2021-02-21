"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации
"""


from uuid import uuid4
import hashlib


class UrlCache:
    __cache = dict()
    __salt: str

    def __init__(self) -> None:
        self.__salt = uuid4().hex

    def get_page_from_hash(self, url: str):
        if url in self.__cache:
            return self.__cache[url]
        else:
            self.__cache[url] = hashlib.sha512(url.encode() + self.__salt.encode()).hexdigest()


url_cache = UrlCache()
url_cache.get_page_from_hash('google.ru')
url_cache.get_page_from_hash('google.ru')
url_cache.get_page_from_hash('google.ru')
