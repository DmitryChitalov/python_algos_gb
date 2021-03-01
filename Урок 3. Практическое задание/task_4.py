"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
from hashlib import sha256
from uuid import uuid4


class UrlCash:
    url_cash: set
    __salt: hex

    def __init__(self):
        self.url_cash = set()
        self.__salt = uuid4().hex
        print(self.__salt)

    def add_url(self, url_address):
        hash_url = sha256(f"{self.__salt}{url_address}".encode('utf-8')).hexdigest()
        # hash_obj1 = sha256(f"mw238v32{passw}87s3gi2d".encode("utf-8"))
        # hash_url = sha256(url_address.encode('utf-8'))hexdigest()
        self.url_cash.add(hash_url)
        print(self.url_cash)

    def check_url(self, url_address):
        check_el = sha256(f"{self.__salt}{url_address}".encode('utf-8')).hexdigest()
        return check_el in self.url_cash

    def len_cash(self):
        return len(self.url_cash)


url_cash = UrlCash()

url_cash.add_url("https://geekbrains.ru/lessons/109785")
url_cash.add_url("https://docs.google.com/document/d/1unkakt07qQTxACBDBVo1n63IgEiLfMx8lkBVnnp-v2A/edit")
url_cash.add_url("https://geekbrains.ru/lessons/109785")
url_cash.add_url("https://pythonworld.ru/tipy-dannyx-v-python/stroki-funkcii-i-metody-strok.html")
url_cash.add_url("https://ru.wikipedia.org/wiki/Python")

print(url_cash.len_cash())
print(url_cash.check_url("https://ru.wikipedia.org/wiki/Python"))
print(url_cash.check_url("https://yandex.ru/"))
