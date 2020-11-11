"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
import hashlib as hl
import binhex as bh


class Cash:

    def __init__(self):
        self.cash_hash = []
        self.cash_storage = []

    def take_url(self, url):
        hash_url = hl.pbkdf2_hmac(
            hash_name='sha256',
            password=url.encode(),
            salt=b'secret',
            iterations=100000
        )
        print(url)
        if not hash_url in self.cash_hash:
            self.cash_storage.append(url)
            self.cash_hash.append(hash_url)


cash = Cash()
cash.take_url(input('Введите URL: '))
cash.take_url(input('Введите URL: '))
cash.take_url(input('Введите URL: '))
print(cash.cash_storage)
