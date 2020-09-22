"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
from hashlib import sha256
from uuid import uuid4

class cache():
    def __init__(self):
        self.cachelist = set()
    def __str__(self):
        return '[' + ', '.join([one_hash for one_hash in self.cachelist]) + ']'

    @staticmethod
    def get_hash(url, salt=False):
        if not salt:
            salt = uuid4().hex
        return sha256(salt.encode() + url.encode() + salt.encode()).hexdigest()

    def check_url(self, url):
        page_hash = self.get_hash(str(url), 'salt')
        if page_hash in self.cachelist:
            return True
        self.cachelist.add(page_hash)

our_pages = cache()

for page in ['https://google.com', 'https://yandex.ru', 'https://geekbrains.ru', 'https://vk.com', 'https://ru.wikipedia.org/']:
    our_pages.check_url(page)

page_1 = 'https://vk.com'
page_2 = 'https://www.youtube.com/'

print(f'Страницы в кэше: {our_pages}')

for new_page in [page_1, page_2]:
    if our_pages.check_url(new_page):
        print(f'Страница {new_page} уже есть в кэше.')
    else:
        print(f'Страница {new_page} добавлена в кэш.')

print(f'Страницы в кэше: {our_pages}')
