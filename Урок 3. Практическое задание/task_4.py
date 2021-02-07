"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
from hashlib import sha256


class CacheWeb:
    def __init__(self):
        self.salt = b'any_salt'
        self.obj = {}

    def get_page(self, url):
        if self.obj.get(url):
            print(f'Данный адрес: {url} присутствует в кэше')
        else:
            res = sha256(self.salt + url.encode()).hexdigest()
            self.obj[url] = res
            print(self.obj)


new_web = CacheWeb()

new_web.get_page('https://habrahabr.ru/')
new_web.get_page('https://habrahabr.ru/')
new_web.get_page('https://google.com/')
new_web.get_page('https://google.com/')



