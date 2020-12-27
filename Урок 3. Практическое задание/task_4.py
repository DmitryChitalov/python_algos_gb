"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
import hashlib


class UrlHash:
    def __init__(self):
        self.cash = {}
        self.salt = 'salt'

    def add_cash(self, url):
        if self.cash.get(url):
            print(f'{url} уже в кэше')
        else:
            self.cash[url] = hashlib.sha256(url.encode() + self.salt.encode()).hexdigest()
            print(f'{url} добавлен в кэш')

    def get_pages(self):
        for i in self.cash.keys():
            print(i)


a = UrlHash()
a.add_cash('youtube.com')
a.add_cash('mail.ru')
a.add_cash('google.ru')
a.add_cash('yandex.ru')
a.add_cash('mail.ru')
a.get_pages()
