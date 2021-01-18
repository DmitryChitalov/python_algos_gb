"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
import hashlib


class Cash:
    salt = '123!@#'

    def __init__(self):
        self.cash = {}
        self.url = None

    def url_hash(self):
        return hashlib.sha256(self.salt.encode() + self.url.encode()).hexdigest()

    def add_cash(self):
        self.cash[self.url] = self.url_hash()


if __name__ == '__main__':

    def add_cash(obj, url_address):
        if obj.cash.get(url_address):
            return f'{url_address} уже добавлен в кэш ранее'
        else:
            obj.url = url_address
            obj.add_cash()
            return f'{url_address} добавлен в кэш'


    cash_url = Cash()
    print(add_cash(cash_url, 'https://e.mail.ru/'))
    print(add_cash(cash_url, 'https://github.com/'))
    print(add_cash(cash_url, 'https://yandex.ru/'))
    print(add_cash(cash_url, 'https://github.com/'))
    # print(cash_url.cash)
