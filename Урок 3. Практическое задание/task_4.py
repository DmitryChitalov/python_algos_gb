"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
from uuid import uuid4
import hashlib


class UrlStorage:
    def __init__(self):
        self.storage = []
        self.salt = uuid4().hex

    def push(self, url):
        url = hashlib.sha256(self.salt.encode() + url.encode()).hexdigest()
        if not self.check(url):
            self.storage.append(url)
        else:
            print('url уже есть в кэше')

    def check(self, url):
        return url in self.storage


if __name__ == '__main__':
    my_url_storage = UrlStorage()
    my_url_storage.push('https://ya.ru')
    my_url_storage.push('https://ya.ru')
    my_url_storage.push('http://mail.ru')
    print(len(my_url_storage.storage))
