"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

from hashlib import sha256


class WebPageLoader:
    def __init__(self):
        self.cache = dict()

    def get_page_content(self, url, salt):
        page_hash = sha256((url + salt).encode('utf-8')).hexdigest()
        page_content = self.cache.get(page_hash)
        if not page_content:
            # тут мы как бы получаем контент страницы
            page_content = 'Never Gonna Give You Up'
            self.cache[page_hash] = page_content
            print('Страница закэширована')
        else:
            print('Возвращаем из кэша')
        return page_content


loader = WebPageLoader()
loader.get_page_content('yandex.ru', 'yandex')
loader.get_page_content('pikabu.ru', 'pikabu')
loader.get_page_content('yandex.ru', 'yandex')
