"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
import hashlib

urls_cashe = {}
salt = 'december'

def url_cashe(url):
    if url in urls_cashe.keys():
        print(f'Адрес {url} уже присутствует в списке страниц')
    else:
        url_c = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        urls_cashe[url] = url_c
        print(urls_cashe)

url_cashe('https://mail.ru/')
url_cashe('https://yandex.ru/')
url_cashe('https://google.com/')
url_cashe('https://mail.ru/')

