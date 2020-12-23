"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
from hashlib import md5


login = "John" """Будем использовать логин для соли"""
cache = {}

def cache_url(url):
    el = md5(url.encode() + login.encode()).hexdigest()
    if el in cache.values():
        print(f'Страница {url} существует, ее хеш - {cache[url]}')
        print(cache)
    else:
        cache[url] = el
        print('Страница добавлена в кэш')
        print(cache)

def startfunc():
    url = input("Введите URL: ")
    cache_url(url)
    startfunc()

startfunc()
