"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
from hashlib import sha256


class UrlGetter:
    def __init__(self):
        self.hash_set = set()

    def get_url(self, url):
        raw_url = url.encode('utf-8')
        salt = url[::-1].encode('utf-8')
        if sha256(raw_url + salt).hexdigest() in self.hash_set:
            print(f'Following url cash - {url}  already inside')
        else:
            self.hash_set.add(sha256(raw_url + salt).hexdigest())

    def show_set(self):
        return [print(i) for i in self.hash_set]


urls_cash = UrlGetter()
urls_cash.get_url(r'https://google.com/')
urls_cash.get_url(r'https://google.ru/')
urls_cash.get_url(r'https://google.com/')
urls_cash.show_set()