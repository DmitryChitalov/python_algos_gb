"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

import hashlib


class Browser:
    def __init__(self):
        self.cache = {}
        self.hash_salt = 'This is salt'.encode('utf-8')

    def open_webpage(self, webpage: str):
        webpage_hash = hashlib.sha256(webpage.encode('utf-8') + self.hash_salt).hexdigest()
        if webpage_hash not in self.cache:
            webpage_data = self.get_webpage_data(webpage)
            self.cache.update({webpage_hash: webpage_data})
        return self.cache[webpage_hash]

    def get_webpage_data(self, webpage: str):
        # Метод получения данных вебстраницы
        return 'data'


internet_explorer = Browser()

internet_explorer.open_webpage('vk.com')
internet_explorer.open_webpage('geekbrains.ru')
internet_explorer.open_webpage('yandex.ru')
internet_explorer.open_webpage('gmail.com')
internet_explorer.open_webpage('vk.com')
internet_explorer.open_webpage('yandex.ru')