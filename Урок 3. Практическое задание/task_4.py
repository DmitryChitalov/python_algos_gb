"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

"""Встроенная функция hash()"""

import hashlib


class UrlCash:
    def __init__(self):
        self.cash_list = []

    def check_cash_list(self, url_hash):
        flag = True
        for i in self.cash_list:
            if i.hexdigest() == url_hash.hexdigest():
                flag = False
        return flag

    def add_url(self, url):
        url_hash = hashlib.sha256(b'UrlCash' + url.encode() + b'UrlCash')
        if self.check_cash_list(url_hash):
            self.cash_list.append(url_hash)
            print(url, ' добавлен в базу кэша')
        else:
            print(url, ' уже находится в кэше')

    def __str__(self):
        return str(self.cash_list)

    def clear(self):
        self.cash_list = []


if __name__ == '__main__':
    base_url = UrlCash()
    base_url.add_url('https://yandex.ru')
    base_url.add_url('https://python-scripts.com')
    base_url.add_url('https://github.com/tryVellum')
    base_url.add_url('https://yandex.ru')
    print(base_url)
    base_url.clear()
    base_url.add_url('https://github.com/tryVellum')

