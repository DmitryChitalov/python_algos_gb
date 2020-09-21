"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете усложнить задачу, реализовав ее через ООП
"""

import hashlib
import uuid


class SavedPages:
    def __init__(self):
        self.pages = set()

    def __str__(self):
        return '[' + ', '.join([one_hash[:6] + '*' for one_hash in self.pages]) + ']'

    @staticmethod
    def _get_hash(url, salt=False):
        '''Генерирует хеш.'''
        if not salt:
            # Генерируем соль.
            salt = uuid.uuid4().hex
        # Получаем хеш.
        return hashlib.sha256(salt.encode() + url.encode() + salt.encode()).hexdigest() + ':' + salt

    def check_page(self, url):
        '''Проверяет страницу на наличие в кэше.'''
        # Получаем хеш.
        page_hash = self._get_hash(str(url), 'salt')
        # Проверяем есть ли такой хеш в кэше.
        if page_hash in self.pages:
            return True
        self.pages.add(page_hash)


our_pages = SavedPages()

# Добавляем страницы.
for page in ['https://vk.com', 'https://google.com', 'https://geekbrains.ru', 'https://yandex.ru', 'https://pypi.org']:
    our_pages.check_page(page)

# Существующая страница.
page_1 = 'https://yandex.ru'
# Новая страница.
page_2 = 'https://www.spacex.com/' 

print(f'Страницы в кэше: {our_pages}')

for new_page in [page_1, page_2]:
    if our_pages.check_page(new_page):
        print(f'[v] Страница {new_page} уже есть в кэше.')
    else:
        print(f'[!] Страница {new_page} добавлена в кэш.')

print(f'Страницы в кэше: {our_pages}')
