"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
import hashlib

g_cash = {}

class PageClass:
    def __init__(self, i_url, i_hash, i_salt):
        self.url  = i_url
        self.hash = i_hash
        self.salt = i_salt

    def __str__(self):
        return self.url + ', ' + self.hash + ', ' + self.salt

def get_from_cash(i_url, i_salt):
    l_hash = hashlib.sha256(i_salt.encode() + i_url.encode('utf-8')).hexdigest()

    l_obj = g_cash.get(l_hash)

    if l_obj is None:
        l_obj = PageClass(i_url, l_hash, i_salt)
        g_cash[l_hash] = l_obj
    else:
        return l_obj


print(get_from_cash('url1', 'salt1'))
print(get_from_cash('url1', 'salt1'))
