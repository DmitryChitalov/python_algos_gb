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


class Cash:

    def __init__(self):
        self.dict = {}
        self.list = []

    def show_cash(self):
        print('')
        print('Кэш лист')
        for self.keys, self.values in self.dict.items():
            print(f'{self.keys}: {self.values}')
        print('')

    def clean_cash(self):
        self.dict = {}
        print('Кэш очищен')

    def check_url_in_cash(self, url):
        salt = uuid4().hex
        hash_url = hashlib.sha256(salt.encode() + url.encode()).hexdigest() + ':' + salt
        self.list = [self.key for self.key in self.dict.keys()]

        if url in self.list:
            print(f'{url} есть в кэше')
            pass
        else:
            self.dict[url] = hash_url
            print(f'адрес {url} добвлен в кэш')


cash_1 = Cash()
cash_1.show_cash()

cash_1.check_url_in_cash('ya.ru')
cash_1.check_url_in_cash('google.com')
cash_1.show_cash()

cash_1.check_url_in_cash('ya.ru')
cash_1.show_cash()

cash_1.clean_cash()
cash_1.check_url_in_cash('geekbrains.ru')
cash_1.show_cash()
