"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
import hashlib


class CacheBase:

    def __init__(self):
        self.cache_base = {}

    def add_link(self, address, files: list):
        cache = hashlib.sha256('some salt'.encode() +
                               address.encode()).hexdigest()
        if cache not in self.cache_base.keys():
            self.cache_base[cache] = files
            print('Страница добавлена')
        else:
            print('Страница уже есть в базе')

    def get_files(self, address):
        cache = hashlib.sha256('some salt'.encode() +
                               address.encode()).hexdigest()
        if cache in self.cache_base.keys():
            return self.cache_base[cache]
        else:
            return 'Такой страницы нет в базе'


new_cache = CacheBase()

new_cache.add_link('https://geekbrains.ru/', ['file_1', 'file_2'])

new_cache.add_link('https://geekbrains.ru/', ['file_1', 'file_2'])
new_cache.add_link('https://github.com/', ['file_3', 'file_4'])

print(new_cache.cache_base)

print(new_cache.get_files('https://geekbrains.ru/'))
print(new_cache.get_files('https://github.com/'))
print(new_cache.get_files('https://qna.habr.com/'))
