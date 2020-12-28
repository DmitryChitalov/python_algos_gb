"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
import hashlib


class Cash(object):
    salt = "This is Salt"

    def __init__(self):
        self.cash = {}

    def add_url(self, url: str):
        hash = hashlib.sha256(self.salt.encode() + url.encode())

        if self.cash.get(url):
            return False

        self.cash[url] = hash

        return True


if __name__ == "__main__":
    cash = Cash()
    print(cash.add_url("github.com"))
    print(cash.add_url("github.com"))