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

    def f_cash(self):
        print('')
        print('Cash list')
        for self.keys, self.values in self.dict.items():
            print(f'{self.keys}: {self.values}')
        print('')

    def f_clean_cash(self):
        self.dict = {}
        print('Cash is empty')

    def f_check_url(self, url):
        salt = uuid4().hex
        hash_url = hashlib.sha256(salt.encode() + url.encode()).hexdigest() + ':' + salt
        self.list = [self.key for self.key in self.dict.keys()]

        if url in self.list:
            print(f'{url} exists in cash')
            pass
        else:
            self.dict[url] = hash_url
            print(f'адрес {url} added in to cash')


cash_1 = Cash()
cash_1.f_cash()

cash_1.f_check_url('yandex.ru')
cash_1.f_check_url('mail.ru')
cash_1.f_cash()

cash_1.f_check_url('yandex.ru')
cash_1.f_cash()

cash_1.f_clean_cash()
cash_1.f_check_url('ya.ru')
cash_1.f_cash()