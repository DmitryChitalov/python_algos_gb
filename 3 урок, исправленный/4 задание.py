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

class caching_web_pages():
    salt = uuid4().hex
    cache = {}
    def url_adress(self, url):
        if self.cache.get(url):
            print(f'Данный адресс: {url} присутствует в кэше.')
        else:
            res = hashlib.sha256(self.salt.encode()).hexdigest()
            self.cache[url] = res
            print(f'Данный адресс внесен в кэш {self.cache}.')
cash_web = caching_web_pages()
cash_web.url_adress('https://vk.com/vkkdanil')
cash_web.url_adress('https://geekbrains.ru/users/765895')
cash_web.url_adress('https://vk.com/vkkdanil')
cash_web.url_adress('https://geekbrains.ru/users/765895')




