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

class a():
    salt = uuid4().hex
    cache = {}
    def f(self, url):
        if self.cache.get(url):
            print(f'Данный адресс: {url} присутствует в кэше.')
        else:
            res = hashlib.sha256(self.salt.encode()).hexdigest()
            self.cache[url] = res
            print(f'Данный адресс внесен в кэш {self.cache}.')
a = a()
a.f('https://vk.com/vkkdanil')
a.f('https://geekbrains.ru/users/765895')
a.f('https://vk.com/vkkdanil')
a.f('https://geekbrains.ru/users/765895')




